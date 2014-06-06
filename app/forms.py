from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, IntegerField
from wtforms.validators import Required

class SJ1Form(Form):
	title = TextField('title')
	content = TextAreaField('content')
	author_name = TextField('author_name')
	topic = TextField('topic')

class SJ2Form(Form):
	title = TextField('title')
	content = TextAreaField('content')
	author_name = TextField('author_name')
	topic = TextField('topic')

class SJ3Form(Form):
	title = TextField('title')
	content = TextAreaField('content')
	author_name = TextField('author_name')
	topic = TextField('topic')