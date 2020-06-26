# import pymysql.cursors
from datetime import datetime
from blog import db
from sqlalchemy.sql import func


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return self.username


class Blog(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    image = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    is_published = db.Column(db.Boolean(), default=True, nullable=False)

    def __repr__(self):
        return self.username

db.create_all()