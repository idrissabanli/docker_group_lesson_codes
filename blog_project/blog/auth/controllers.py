from flask import Blueprint, render_template, request, redirect, session
from blog.auth.forms import RegisterForm, LogInForm
from blog.auth.models import create_user, check_user
from wtforms import ValidationError

auth = Blueprint(__name__, 'auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    next_page = request.args.get('next', '/')
    form_error_message = None
    if request.method == 'POST' and form.validate_on_submit():
        user = check_user(form.data['username'], form.data['password'])
        if user:
            session['user_id'] = user['id']
            session['loginned'] = True
            return redirect(next_page)
        else:
            form_error_message = 'User not found'
    context = {
        'form': form,
        'form_error_message': form_error_message
    }
    return render_template('auth/login.html', **context)

"""
| kod | data |
   1  |   loginned = True, user_data=idris   |
   2  |   loginned = False, user_data=aqil   |
"""
    



@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        create_user(**form.data)
        return redirect('/')
    context = {
        'form': form
    }
    return render_template('auth/register.html', **context)
