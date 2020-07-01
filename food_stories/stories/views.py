from django.shortcuts import render
from stories.models import Category, Recipe

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

