from flask import Flask
from blog.core.controllers import core
from blog.auth.controllers import auth

app = Flask(__name__, static_url_path='/static')

app.register_blueprint(core)
app.register_blueprint(auth)
