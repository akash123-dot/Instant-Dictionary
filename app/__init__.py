from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class CreateApp:
    
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'your-secret-key'
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(self.app)

        from app import models
        from app.auth.auth import auth_bp
        from app.main.app import main_app
        from app.api_logic.api_logic import api_bp

        self.app.register_blueprint(auth_bp, url_prefix='/auth')
        self.app.register_blueprint(main_app, url_prefix='/')
        self.app.register_blueprint(api_bp, url_prefix='/api')

    
    def getapp(self):
        return self.app