from flask import render_template, Blueprint, g
from flask_babel import _, refresh
from app import app

multilingual = Blueprint('multilingual', __name__, template_folder='templates')

@multilingual.route('/')
@multilingual.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': _('Beautiful day in Portland!')
        },
        {
            'author': {'username': 'Susan'},
            'body': _('The Avengers movie was so cool!')
        }
    ]
    return render_template('multilingual/index.html', title=_('Home'), user=user, posts=posts)

@multilingual.route('/cake')
def cake():
    g.lang_code = 'en'
    refresh()
    return render_template('multilingual/cake.html', title=_('The Cake is a Lie'))