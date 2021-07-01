from logging import error
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['Comprar café', 'Enviar solicitud de compra', 'Entregar video al productor']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)

# @app.route('/')
# def index():
#     user_ip = request.remote_addr

#     response = make_response(redirect('/hello'))
#     response.set_cookie('user_ip', user_ip)
 
#     return response

@app.route("/")
def index():
    raise(Exception('500 Error'))

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip':user_ip,
        'todos':todos
    }

    return render_template('hello.html', **context)

