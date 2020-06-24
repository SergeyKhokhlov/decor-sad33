from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    full_name = StringField('ФИО', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('пароль', validators=[DataRequired()])
    repeat_password = PasswordField('повторите пароль', validators=[DataRequired()])
    submit = SubmitField('войти')
