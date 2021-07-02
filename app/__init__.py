from flask import Flask
from .config import Config 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['WTF_CSRF_ENABLED']= True

    return app