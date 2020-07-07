from django.shortcuts import render, redirect, get_object_or_404
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

def contact(request):
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


def recipes(request):
    recipes = Recipe.objects.filter(is_published=True)
    context = {
        'recipes': recipes
    }
    return render(request, 'recipes.html', context)


def recipe_detail(request, slug):
    print(slug)
    # recipe = Recipe.objects.get(slug=slug)
    recipe = get_object_or_404(Recipe, slug=slug)
    context = {
        'object': recipe
    }
    return render(request, 'single.html', context)



