#models.py

from app import db

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100))
	content = db.Column(db.Text)
	author_name = db.Column(db.Text)
	topic = db.Column(db.Text)
