from flask import Blueprint, render_template, request, redirect, flash
from blog.core.models import create_blog, all_blogs

core = Blueprint(__name__, 'core', static_url_path='idris/')

@core.route('/')
def home():
    blogs = all_blogs()
    context = {
        'blogs': blogs
    }
    return render_template('core/index.html', **context)

@core.route('/create', methods=['GET', 'POST'])
def create():
    print(request.form)
    print(request.method)
    if request.method == 'POST':
        # create_blog(title=request.form['title'], description=request.form['description'], owner_name=request.form['owner_name'], image='')
        create_blog(**request.form, image='')
        flash('Blog successfully created')
        return redirect('/')
    return render_template('core/create.html')
