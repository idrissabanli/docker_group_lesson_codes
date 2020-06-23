from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class RegisterForm(FlaskForm):
    username = StringField('Istifadeci adi', validators=[Length(5, 50), DataRequired()])
    email = StringField('E pocht', validators=[Email(), Length(max=40), DataRequired()])
    first_name = StringField('Ad', validators=[Length(max=40), DataRequired()])
    surname = StringField('Soyad', validators=[Length(max=40), DataRequired()])
    password = PasswordField('Sifre', validators=[Length(max=40), DataRequired()])
