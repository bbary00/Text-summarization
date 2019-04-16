from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap
from transforming import summarize
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, \
    logout_user, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:060800Bodia@localhost/press'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    text = db.relationship("Text", backref='user')
    summary = db.relationship("Summary", backref='user')


class Text(db.Model):
    __tablename__ = 'text'
    text = db.Column(db.String())
    text_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    summary = db.relationship("Summary", backref='text')

class Summary(db.Model):
    __tablename__ = 'summary'
    sum_id = db.Column(db.Integer, primary_key=True)
    sum = db.Column(db.String())
    text_id = db.Column(db.Integer, db.ForeignKey('text.text_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(),
                                                   Length(min=4, max=15)],
                           render_kw={"placeholder":"Username"})
    password = PasswordField('password', validators=[InputRequired(),
                                                     Length(min=8, max=80)],
                             render_kw={"placeholder":"Password"})
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(),
                                             Email(message='Invalid email'),
                                             Length(max=50)],
                        render_kw={"placeholder":"Email"})
    username = StringField('username', validators=[InputRequired(),
                                                   Length(min=4, max=15)],
                           render_kw={"placeholder":"Username"})
    password = PasswordField('password', validators=[InputRequired(),
                                                     Length(min=8, max=80,
                                                            message='HUY')],
                             render_kw={"placeholder":"Password"})


@app.route('/')
def main_route():
    if current_user.is_authenticated:
         return render_template("index_for_users.html")
    else:
         return render_template("index_for_anonymous.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('main_route'))

        return '<h1>Invalid username or password</h1>'
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


@app.route('/summarization', methods=['POST'])
def summary():
    user_id = current_user
    data = request.form['text']
    new_text = Text(text=data, user=user_id)
    db.session.add(new_text)
    db.session.commit()
    sent = request.form['sentence']
    summ = summarize(data, sent)
    new_summary = Summary(sum=summ, user=user_id, text=new_text)
    db.session.add(new_summary)
    db.session.commit()
    return jsonify(summ)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data,
                                                 method='sha256')
        new_user = User(username=form.username.data, email=form.email.data,
                        password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_route'))


if __name__ == '__main__':
    app.run(debug=True)
