from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, \
    TemplateView
from django.urls import reverse_lazy

from stories.models import Category, Recipe, Story
from stories.forms import ContactForm, StoryForm
from django.contrib import messages


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


class CreateStoryView(CreateView):
    form_class = StoryForm
    template_name = 'create_story.html'

    def form_valid(self, form):
        story = form.save(commit=False)
        story.author = self.request.user
        story.save()
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



