from flask import Flask

from .config import Config 
from .auth import auth

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['WTF_CSRF_ENABLED']= True
    app.register_blueprint(auth)

    return app
