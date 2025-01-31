import os
from flask_sqlalchemy import SQLAlchemy
    
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_clave_secreta_muy_segura'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///web_fp.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False