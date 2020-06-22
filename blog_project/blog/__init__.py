from flask import Flask
from blog.core.controllers import core

app = Flask(__name__, static_url_path='/static')

app.register_blueprint(core)
