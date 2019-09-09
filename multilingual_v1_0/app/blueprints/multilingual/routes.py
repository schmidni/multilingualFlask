from flask import render_template, Blueprint, g, redirect, request, current_app, abort, url_for
from flask_babel import _, refresh
from multilingual_v1_0.app import app

multilingual = Blueprint('multilingual', __name__, template_folder='templates', url_prefix='/<lang_code>')

@multilingual.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

@multilingual.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')

@multilingual.before_request
def before_request():
    if g.lang_code not in current_app.config['LANGUAGES']:
        adapter = app.url_map.bind('')
        try:
            endpoint, args = adapter.match('/en' + request.full_path.rstrip('/ ?'))
            return redirect(url_for(endpoint, **args), 301)
        except:
            abort(404)

    dfl = request.url_rule.defaults
    if 'lang_code' in dfl:
        if dfl['lang_code'] != request.full_path.split('/')[1]:
            abort(404)

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

@multilingual.route('/cake', defaults={'lang_code': 'en'})
@multilingual.route('/kuchen', defaults={'lang_code': 'de'})
@multilingual.route('/gateau', defaults={'lang_code': 'fr'})
def cake():
    return render_template('multilingual/cake.html', title=_('The Cake is a Lie'))