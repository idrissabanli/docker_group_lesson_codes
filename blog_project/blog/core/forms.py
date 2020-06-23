from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class BlogForm(FlaskForm):
    title = StringField('Basligi', validators=[Length(min=3, max=255, ), DataRequired()])
    description = TextAreaField('Mezmun', validators=[Length(min=3), DataRequired()])
    owner_name = StringField('Muellif', validators=[Length(min=3, max=50), DataRequired()])
    # recaptcha = RecaptchaField()