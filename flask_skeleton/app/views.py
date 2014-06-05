# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
def index():
	return ("This is our Social Justice App skeleton, people!")


