from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, \
    TemplateView, View
from django.urls import reverse_lazy

from stories.models import Category, Recipe, Story, SavedArticle
from stories.forms import ContactForm, StoryForm, RecipeForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, HttpResponse
from django.core.exceptions import PermissionDenied

# def home(request):
#     categories = Category.objects.all()[:3]
#     recipes = Recipe.objects.all()[:2]
#     context = {
#         'categories': categories,
#         'recipes': recipes
#     }
#     return render(request, 'index.html', context)


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        context['recipes'] = Recipe.objects.all().order_by('-show_home_page')[:2]
        context['categories'] = Category.objects.all()[:3]
        return context


def about(request):
    return render(request, 'about.html', )


def manage(request):
    return render(request, 'manage.html')

# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Mesajiniz gonderildi!!')
#             return redirect('/')
#         else:
#             messages.error(request, 'Mesajiniz gonderilmedi')
#     else:
#         form = ContactForm()
#     context = {
#         'form' : form
#     }
#     return render(request, 'contact.html', context)


class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Mesajiniz gonderildi!!')
        return super().form_valid(form)


class CreateStoryView(LoginRequiredMixin, CreateView):
    form_class = StoryForm
    template_name = 'create_story.html'

    def form_valid(self, form):
        story = form.save(commit=False)
        story.author = self.request.user
        story.save()
        return super().form_valid(form)

from django.contrib.auth.mixins import PermissionRequiredMixin

class CreateRecipeView(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = 'create_recipe.html'
    # permission_required = ('stories.add_recipe',)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_author:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.author = self.request.user
        recipe.save()
        return super().form_valid(form)


def recipes(request):
    recipes = Recipe.objects.filter(is_published=True)
    context = {
        'recipes': recipes
    }
    return render(request, 'recipes.html', context)


class StoryListView(ListView):
    model = Story
    template_name = 'stories.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class StoryDetailView(DetailView):
    model = Story # context object ve story adlari ile template fetch
    template_name = 'single.html'
    # context_object_name = 'story_detail'


class StoryUpdateView(UpdateView):
    form_class = StoryForm
    model = Story
    template_name = 'create_story.html'


class StoryDeleteView(DeleteView):
    model = Story
    success_url = reverse_lazy('stories')
    http_method_names = ('get',)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def recipe_detail(request, slug):
    print(slug)
    # recipe = Recipe.objects.get(slug=slug)
    recipe = get_object_or_404(Recipe, slug=slug)
    context = {
        'object': recipe
    }
    return render(request, 'single.html', context)

class SaveRecipeView(View):
    def get(self, *args, **kwargs):
        recipe_id = kwargs.get('pk')
        message = 'Melumat elave edildi'
        recipe = get_object_or_404(Recipe, id=recipe_id)
        
        if self.request.user.is_authenticated:
            save_article, created = SavedArticle.objects.get_or_create(user=self.request.user, recipe=recipe)
            if not created:
                message = 'Melumat evvel elave edilmisdi'
            response = HttpResponse(message)
        else:
            saved_articles = self.request.COOKIES.get('saved_articles', '')
            print('saved_articles', saved_articles)
            if str(recipe_id) not in saved_articles.split(';'):
                saved_articles += str(recipe_id) + ";"
            response = HttpResponse(message)
            response.set_cookie('saved_articles', saved_articles)
        # messages.success(self.request, message)
        return response


class SavedRecipeListView(ListView):
    model = Recipe
    template_name = 'saved_recipes.html'
    context_object_name = 'recipes'

    def get_queryset(self, ):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
            user_saved_articles_ids = self.request.user.saved_articles.values_list('id', flat=True)
            return queryset.filter(id__in=user_saved_articles_ids)
        else:
            saved_recipes = self.request.COOKIES.get('saved_articles')
            if saved_recipes:
                saved_recipe_ids = [int(id) for id in saved_recipes.split(';') if id and id != 0]
                queryset = super().get_queryset()
                return queryset.filter(id__in=saved_recipe_ids)
            return None
