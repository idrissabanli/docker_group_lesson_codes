from flask import Flask, session, send_from_directory
from flask_login import LoginManager
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3306/blog_project_orm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

BASE_DIRS = os.path.dirname(os.path.abspath(__file__)) # home/idris/blblog.__init__.py
print(BASE_DIRS)
UPLOADED_FILES_DIR = os.path.join(BASE_DIRS, 'media')
app.config['UPLOAD_FOLDER'] = UPLOADED_FILES_DIR

if not os.path.isdir(UPLOADED_FILES_DIR):
    os.mkdir(UPLOADED_FILES_DIR)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOADED_FILES_DIR,
                               filename)


db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "blog.auth.controllers.login"

from blog.auth.controllers import auth
from blog.core.controllers import core


app.register_blueprint(auth)
app.register_blueprint(core)


