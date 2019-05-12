from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators \
    import InputRequired, Email, Length, ValidationError, EqualTo
from models import User


class Unique(object):

    """ validator that checks field uniqueness"""

    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        if not message:
            message = u'this element already exists'
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

    def is_unique(self, field):
        check = self.model.query.filter(self.field == field).first()
        if check:
            return False
        return True


class LoginForm(FlaskForm):

    """
    User login form
    """
    username = StringField('username',
                           validators=[InputRequired(),
                                       Length(min=4, max=15,
                                              message="Invalid username")],
                           render_kw={"placeholder": "Username"})
    password = PasswordField('password',
                             validators=[InputRequired(),
                                         Length(min=8, max=30,
                                                message="Invalid password")],
                             render_kw={"placeholder": "Password"})
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):

    """
    User registration form
    """

    email = StringField('email',
                        validators=[InputRequired(),
                                    Email(message='Invalid email'),
                                    Length(max=50),
                                    Unique(User, User.email,
                                    message="User with this email already "
                                            "exists.")],
                        render_kw={"placeholder": "Email"})
    username = StringField('username',
                           validators=[InputRequired(),
                                       Length(min=4, max=15,
                                              message="Username must be "
                                                      "between 4 and 15 "
                                                      "characters."),
                                       Unique(User, User.username,
                                       message="User with this username "
                                               "already exists.")],
                           render_kw={"placeholder": "Username"})
    password = PasswordField('password',
                             render_kw={"placeholder": "Password"},
                             validators=[InputRequired(),
                                         Length(min=8, max=30,
                                                message="Password must be "
                                                        "between 8 and 30 "
                                                        "characters."),
                                         EqualTo('confirm',
                                                 message='Passwords must '
                                                         'match')])
    confirm = PasswordField('Repeat Password',
                            render_kw={"placeholder": "Repeat Password"})
