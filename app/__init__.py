from flask import Flask
app = Flask(__name__)

from app.blueprints.multilingual import multilingual

app.register_blueprint(multilingual)