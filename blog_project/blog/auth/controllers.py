from flask import Blueprint, render_template
from blog.auth.forms import RegisterForm


auth = Blueprint(__name__, 'auth')


@auth.route('/register')
def register():
    form = RegisterForm()

    context = {
        'form': form
    }
    return render_template('auth/register.html', **context)
