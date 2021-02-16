from app import db
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    posts = db.relationship('Post', backref='post', lazy=True)
    

    def __init__(self, first_name, last_name, password):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = f'{self.first_name}{self.last_name[0]}@codingtemple.com'.lower()

    def create_password_has(self, password):
        self.password = generate_password_hash(password)

    def verify_password_hash(self):
        return check_password_hash(password)

    def __repr__(self):
        return f'<User: {self.email}>'

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.Text)
    date_created = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    date_updated = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.ForeignKey('user.user_id'))

    def __repr__(self):
        return f'<Post: ID: {self.id} {self.title}>'