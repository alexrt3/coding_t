from app import db
import datetime from datetime as dt

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, first_name, last_name, password):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = f'{self.first_name}{self.last_name[0]}@codingtemple.com'.lower()

    def __repr__(self):
        return f'<User: {self.email}>'

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.Text)
    date_created = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    date_updated = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Post: ID: {self.id} {self.title}>'