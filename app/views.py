# -*- coding: utf-8 -*-

from flask import render_template
from app import app  # Go get stuff we need from the app folder
from models import Post
from forms import SJ1Form, SJ2Form, SJ3Form

@app.route('/')
def index():
	posts = Post.query.all()
	return render_template('index.html', posts = posts)

@app.route('/first_issue')
def first_view():
	form = SJ1Form
	return render_template('sj1.html', form=form)

@app.route('/second_issue')
def second_view():
	form = SJ2Form
	return render_template('sj2.html', form=form)

@app.route('/third_issue')
def third_view():
	form = SJ3Form
	return render_template('sj3.html', form=form)

