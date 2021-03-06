# from logging import error
from flask import request, make_response, redirect, render_template, session
import unittest

from app import create_app

app = create_app()

todos = ['Comprar café', 'Enviar solicitud de compra', 'Entregar video al productor']

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

@app.route('/', methods=['GET'])
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@app.route('/hello', methods=['GET'])
def hello():
    user_ip = session.get('user_ip')
    username = session.get('username')
    print('UNERNAME: '+str(username))
    print('USER-IP: '+str(user_ip))
    
    context = {
        'user_ip':user_ip,
        'todos':todos,
        'username':username
    }

    return render_template('hello.html', **context)

## END