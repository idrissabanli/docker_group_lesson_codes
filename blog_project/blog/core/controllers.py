from flask import Blueprint, render_template, request, redirect, flash, session
from blog.core.models import create_blog, all_blogs, get_blogs_count
from blog.core.forms import BlogForm, ContactForm
from blog.core.utils import login_required
from blog import Contact, db
import math

core = Blueprint(__name__, 'core', static_url_path='idris/')

@core.route('/')
def home():
    page = int(request.args.get('page', 1))
    print(page)
    blogs = all_blogs((page-1)*2, 2)
    page_count = math.ceil(get_blogs_count()/2)
    page_range = range(1, page_count+1)
    next_page = None
    previous_page = None
    if page+1 <= page_count:
        next_page = page+1
    if page-1 >= 0:
        previous_page = page-1
    context = {
        'blogs': blogs,
        'page_range': page_range, 
        'next_page': next_page,
        'previous_page': previous_page,
        'current_page': page,
    }
    return render_template('core/index.html', **context)

@core.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = BlogForm()
    if form.validate_on_submit():
        print(form.data)
        create_blog(**form.data, user_id=session.get('user_id'), image='')
        flash('Melumat elave edildi')
        return redirect('/')
    context = {
        'form': form
    }
    return render_template('core/create.html', **context)

@core.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact_info = Contact(username=form.username.data, email=form.email.data, subject=form.subject.data, message=form.message.data)
        db.session.add(contact_info)
        db.session.commit()
        flash('Mesajiniz gonderildi')
        return redirect('/')
    context = {
        'form': form
    }
    return render_template('core/contact.html', **context)


@core.route('/faqs')
def faqs():
    questions = Contact.query.all()
    print(questions)
    context = {
        'questions': questions
    }
    return render_template('core/faqs.html', **context)

    # if request.method == 'POST':
    #     # create_blog(title=request.form['title'], description=request.form['description'], owner_name=request.form['owner_name'], image='')
    #     create_blog(**request.form, image='')
    #     flash('Blog successfully created')
    #     return redirect('/')
    
