from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, Required, Email, EqualTo

class SignupUser(FlaskForm):
    username = StringField("Username", validators = [Length(min = 2, max = 30), Required()])
    email = StringField("Email", validators = [Email(), Required()])
    password = PasswordField("Password", validators = [Required()])
    confirm_password = PasswordField("Confirm Password", validators = [EqualTo('password')])
    submit = SubmitField("Sign up")


class SigninUser(FlaskForm):
    email = StringField("Email", validators = [Required(), Email()])
    password = PasswordField("Password", validators = [Required()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign in")