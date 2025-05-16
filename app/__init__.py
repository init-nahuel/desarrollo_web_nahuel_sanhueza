from flask import Flask
from app.routes import main

UPLOAD_FOLDER = 'static/img'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(main.main_routes)
