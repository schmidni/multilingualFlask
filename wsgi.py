from werkzeug.wsgi import DispatcherMiddleware
from multilingual_v0_6.app import app as app06
from multilingual_v1_0.app import app as app10

application = DispatcherMiddleware({'/lang0.6': app06}, {'/lang1.0':app10})