# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tenant_apartment_system.db'  # SQLite DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
