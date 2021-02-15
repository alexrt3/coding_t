import os 
from dotenv import load_dotenv

basedir = os.path.abspath(os.dirname(__name__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')