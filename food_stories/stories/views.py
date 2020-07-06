from django.shortcuts import render, redirect
from stories.models import Category, Recipe
from stories.forms import ContactForm
from django.contrib import messages

def home(request):
    categories = Category.objects.all()[:3]
    recipes = Recipe.objects.all()[:2]
    context = {
        'categories': categories,
        'recipes': recipes
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html', )

def contant(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajiniz gonderildi!!')
            return redirect('/')
        else:
            messages.error(request, 'Mesajiniz gonderilmedi')
    else:
        form = ContactForm()
    context = {
        'form' : form
    }
    return render(request, 'contact.html', context)

