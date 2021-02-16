from app import app
from flask import render_template, Post
from app.models import User


@app.route('/')
def index():
    context = {
        'posts': Post.query.all()
    }
    return render_template('home.html', **context)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

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