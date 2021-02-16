from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import migrate


app = Flask(__name__)

from app import views