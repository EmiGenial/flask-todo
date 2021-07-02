from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    input={'class':'input is-small mt-1'}
    button={'class':'button is-primary mt-5'}
    username = StringField('Nombre de usuario', validators=[DataRequired()], render_kw=input)
    password = PasswordField('Password', validators=[DataRequired()], render_kw=input)
    submit = SubmitField('Login', render_kw=button)