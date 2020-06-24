from flask import Blueprint, render_template, request, redirect, flash, session
from blog.core.models import create_blog, all_blogs
from blog.core.forms import BlogForm
from blog.core.utils import login_required

core = Blueprint(__name__, 'core', static_url_path='idris/')

@core.route('/')
@login_required
def home():
    blogs = all_blogs()
    context = {
        'blogs': blogs
    }
    return render_template('core/index.html', **context)

@core.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = BlogForm()
    if form.validate_on_submit():
        print(form.data)
        create_blog(**form.data, image='')

    context = {
        'form': form
    }
    return render_template('core/create.html', **context)
    # if request.method == 'POST':
    #     # create_blog(title=request.form['title'], description=request.form['description'], owner_name=request.form['owner_name'], image='')
    #     create_blog(**request.form, image='')
    #     flash('Blog successfully created')
    #     return redirect('/')
    
