from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
	user =  {'username': 'miguel'}
	posts = [
		{
			'author': {'username': 'Jora'},
			'body': 'Kak je horosho!'
		},
		{
			'author': {'username': 'Jenya'},
			'body': 'Deistvitelno!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)