# -*- coding: utf-8 -*-

from flask import render_template
from app import app  # Go get stuff we need from the app folder
from models import Post, User

@app.route('/')
def index():
	users = User.query.all()
	posts = Post.query.all()
	return render_template('index.html', users = users, posts = posts)

@app.route('/first_issue')
def second_view():
	return render_template('sj1.html')

@app.route('/second_issue')
def third_view():
	return render_template('sj2.html')

@app.route('/third_issue')
def third_view():
	return render_template('sj3.html')


