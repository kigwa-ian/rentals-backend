from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize app
app = Flask(__name__)

# Set up database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional: Disables a feature that you don’t need.

# Initialize SQLAlchemy
db = SQLAlchemy()
db.init_app(app)  # <-- This is important, it binds SQLAlchemy to the app

# Initialize Marshmallow
ma = Marshmallow(app)

# Your models and routes go here...
