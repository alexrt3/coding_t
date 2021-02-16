from app import app
from flask import render_template
from app.models import User, Post


@app.route('/')
def home():
    context = {
        'posts': Post.query.all()
    }
    return render_template('home.html', **context)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/explore')
def explore():
    context = {
        'users': User.query.all()
    }
    return render_template('explore.html', **context)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')