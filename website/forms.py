from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class ResetRequestForm(FlaskForm):
    email = StringField(label='email',validators=[DataRequired()])
    submit = SubmitField(label='Reset Password', validators=[DataRequired()])


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Enter New Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Reset')
