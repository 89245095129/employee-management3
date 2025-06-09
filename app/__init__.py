# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config  # Импорт Config должен быть в начале

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):  # Теперь Config определен
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.routes import bp
    app.register_blueprint(bp)
    
    return app

