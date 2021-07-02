# from logging import error
from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secreto'
app.config['WTF_CSRF_ENABLED']= True

todos = ['Comprar café', 'Enviar solicitud de compra', 'Entregar video al productor']

class LoginForm(FlaskForm):
    input={'class':'input is-small mt-1'}
    button={'class':'button is-primary mt-5'}
    username = StringField('Nombre de usuario', validators=[DataRequired()], render_kw=input)
    password = PasswordField('Password', validators=[DataRequired()], render_kw=input)
    submit = SubmitField('Login', render_kw=button)

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    
    return response

@app.route('/hello', methods=['POST','GET'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context = {
        'user_ip':user_ip,
        'todos':todos,
        'login_form':login_form,
        'username':username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('Registrado con éxito!', category='is-primary is-light')
        return redirect(url_for('index'))

    return render_template('hello.html', **context)

