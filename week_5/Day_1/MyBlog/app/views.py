from app import app, db
from flask import render_template, request, redirect, url_for
from app.models import User, Post


@app.route('/')
def home():
    context = {
        'posts': Post.query.order_by(Post.date_created.desc()).all()
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

@app.route('/register', methods=['GET', 'Post'])
def register():
    if request.method == 'POST':
        res= request.form
        if res['confirm_password'] == res['password']:
            u = User(first_name=res['first_name'], last_name=res['last_name'], password=res['password'])
            db.session.add(u)
            db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')