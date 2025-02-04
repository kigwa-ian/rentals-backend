from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from .routes import main_routes  # Import routes from where you define your API

# Initialize the instances
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database_name.db'  # Replace with your database URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)  # Enable CORS for cross-origin requests

    db.init_app(app)  # Initialize the db instance
    migrate.init_app(app, db)  # Initialize the migrate instance

    app.register_blueprint(main_routes)  # Register routes

    return app
