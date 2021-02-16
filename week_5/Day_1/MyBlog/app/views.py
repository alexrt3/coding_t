from app import app, data
from flask import render_template


@app.route('/')
def home():
    context = {
        'posts': data.posts
    }
    return render_template('home.html', **context)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')