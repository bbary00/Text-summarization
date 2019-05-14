# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, request, jsonify, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, \
    logout_user, current_user
from transforming import summarize
from forms import RegisterForm, LoginForm, Unique
from models import User, Text, Summary, Saved, db, app


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    """Initialize user in query"""
    return User.query.get(int(user_id))


@app.route('/')
def main_route():

    """
    Function that redirect authenticated and not authenticated user
    in an appropriate page.
    """

    if current_user.is_authenticated:
        return render_template("index_for_users.html")
    else:
        return render_template("index_for_anonymous.html")


@app.route('/profile')
def profile():
    """Return user's cabinet"""

    if not current_user.is_authenticated:
        return login()
    return render_template("profile.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    """
    Sign in function
    """

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main_route'))
            else:
                flash("Password is wrong.")
        else:
            flash("Wrong username or password.")
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():

    """
    Function for user registration.
    """

    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data,
                                                 method='sha256')
        new_user = User(username=form.username.data, email=form.email.data,
                        password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/summarization', methods=['POST'])
def summary():

    """
    Summarization function with saving data to DB
    for authenticated user.
    """

    data = request.form['text']
    sent = request.form['sentence']
    perc = request.form['percentage']
    summ = summarize(data, sent, perc)
    total_words_text = str(len(data.split()))
    total_words_summary = str(len(summ.split()))
    if current_user.is_authenticated:
        user_id = current_user
        new_text = Text(text=data, user=user_id, total_words=total_words_text)
        new_summary = Summary(sum=summ, user=user_id,
                              text=new_text, total_words=total_words_summary)
        db.session.add(new_text)
        db.session.add(new_summary)
        db.session.commit()
        return jsonify(summ)
    return jsonify(summ)


@app.route('/db_info', methods=['POST'])
def get_db_info():

    """
    Get all user's texts and summaries from DB
    and send then ordered by date in JSON format
    """

    u_id = current_user
    text_data = Text.query.filter_by(user_id=u_id.id).all()
    summ_data = Summary.query.filter_by(user_id=u_id.id).all()
    saved_data = Saved.query.filter_by(user_id=u_id.id).all()
    total_text = sum([int(txt.total_words) for txt in text_data])
    total_sum = sum([int(summ.total_words) for summ in summ_data])
    saved_words = total_text - total_sum
    minutes = saved_words // 150
    saved_time = '{:02d}:{:02d}:{:02d}'.format(minutes // (60*24),
                                               (minutes % (60*24)) // 60,
                                               (minutes % (60*24)) % 60)

    page_data = {
        "user_name": current_user.username,
        "saved_time": saved_time,
        "saved_words": saved_words
    }

    last_10 = dict()
    my_range = min(10, len(text_data)) + 1
    for i in range(1, my_range):
        last_10[str(i)] = summ_data[-i].sum

    user_saved_data = dict()
    saved_len = len(saved_data)
    for i, obj in enumerate(saved_data):
        user_saved_data[saved_len - i] = {obj.summary: obj.text}

    to_write = {
        "page_data": page_data,
        "last_10": last_10,
        "saved_data": user_saved_data
    }
    return jsonify(to_write)


@app.route('/save', methods=['POST'])
def save():
    text = request.form['text']
    summ = request.form['summary']
    if not Unique(Saved, Saved.summary).is_unique(summ):
        return "This text is already saved."
    user_id = current_user
    new_save = Saved(text=text, user=user_id, summary=summ)
    db.session.add(new_save)
    db.session.commit()
    return "Saved."


@app.route('/logout')
@login_required
def logout():
    """Logout and redirect to appropriate page."""
    logout_user()
    return redirect(url_for('main_route'))


if __name__ == '__main__':
    app.run(debug=True)
