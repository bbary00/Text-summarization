from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from sqlalchemy.sql import func


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


class User(UserMixin, db.Model):

    """
    Class used for describing "user" table in database
    """

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    text = db.relationship("Text", backref='user')
    summary = db.relationship("Summary", backref='user')
    saved = db.relationship("Saved", backref='user')


class Text(db.Model):

    """
    Class used for describing "text" table in database
    """

    __tablename__ = 'text'
    text = db.Column(db.String())
    total_words = db.Column(db.String())
    text_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    summary = db.relationship("Summary", backref='text')


class Summary(db.Model):

    """
    Class used for describing "summary" table in database
    """

    __tablename__ = 'summary'
    sum_id = db.Column(db.Integer, primary_key=True)
    sum = db.Column(db.String())
    total_words = db.Column(db.String())
    text_id = db.Column(db.Integer, db.ForeignKey('text.text_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Saved(db.Model):

    """
    Class used for describing "saved" table in database
    """

    __tablename__ = 'saved'
    text = db.Column(db.String())
    summary = db.Column(db.String())
    saved_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
