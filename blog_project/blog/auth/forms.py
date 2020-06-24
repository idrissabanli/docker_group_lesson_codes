from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, Email
from blog.auth.models import check_user_username, check_user_email


class LogInForm(FlaskForm):
    username = StringField('Istifadeci adi', validators=[Length(5, 50), DataRequired()])
    password = PasswordField('Sifre', validators=[Length(min=8, max=40), DataRequired()])


class RegisterForm(FlaskForm):
    username = StringField('Istifadeci adi', validators=[Length(5, 50), DataRequired()])
    email = StringField('E pocht', validators=[Email(), Length(max=40), DataRequired()])
    first_name = StringField('Ad', validators=[Length(max=40), DataRequired()])
    surname = StringField('Soyad', validators=[Length(max=40), DataRequired()])
    password = PasswordField('Sifre', validators=[Length(min=8, max=40), DataRequired()])

    def validate_username(self, field):
        if check_user_username(field.data):
            raise ValidationError('Username already taken')
        return field

    def validate_email(self, field):
        if check_user_email(field.data):
            raise ValidationError('Email already taken')
        return field

    def validate_password(self, field):
        data = field.data
        print(data)
        for letter in data:
            print(ord(letter))
        cap_letter = [letter for letter in data if 65 <= ord(letter) <= 90]
        print(cap_letter)
        if data.isdigit():
            raise ValidationError('Herif yaz')
        elif not cap_letter:
            raise ValidationError('Boyuk herif olmalidir')
        return field

