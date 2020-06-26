# from flask import session, redirect, flash, request
from flask import url_for
from blog import UPLOADED_FILES_DIR, os
from werkzeug.utils import secure_filename
from datetime import datetime


def save_file(f):
    filename = secure_filename(f.filename)
    filename = f'{datetime.now()}_{filename}'
    file_dir = os.path.join(
        UPLOADED_FILES_DIR, filename
    )
    f.save(file_dir)
    file_path = url_for('uploaded_file', filename=filename) # '/uploads/<filename>'
    return file_path