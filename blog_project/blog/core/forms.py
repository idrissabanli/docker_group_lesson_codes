from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Length

class BlogForm(FlaskForm):
    title = StringField('Basligi', validators=[Length(min=3, max=255, ), DataRequired()])
    description = TextAreaField('Mezmun', validators=[Length(min=3), DataRequired()])
    image = FileField(label='Sekil', validators=[FileRequired()])

class ContactForm(FlaskForm):
    username = StringField(validators=[Length(min=3, max=40, ), DataRequired()])
    email = StringField(validators=[Length(min=3, max=40, ), DataRequired()])
    subject = StringField(validators=[Length(min=3, max=255, ), DataRequired()])
    message = TextAreaField(validators=[DataRequired()])