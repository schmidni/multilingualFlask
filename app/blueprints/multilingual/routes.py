from flask import render_template, Blueprint
from app import app

multilingual = Blueprint('multilingual', __name__, template_folder='templates')


@multilingual.route('/')
@multilingual.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('multilingual/index.html', title='Home', user=user, posts=posts)

