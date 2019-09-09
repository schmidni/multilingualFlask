from werkzeug.wsgi import DispatcherMiddleware
from multilingual_v0_6.app import app as app06
from multilingual_v1_0.app import app as app10

def null_app(environ, start_response):
    start_response('404 Not Found', [('Content-Type', 'text/plain')])
    return ['Not Found']

application = DispatcherMiddleware(null_app, {'/lang10':app10, '/lang06':app06})
