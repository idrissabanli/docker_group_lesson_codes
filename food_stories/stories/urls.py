from django.urls import path
from stories.views import HomePage, about, recipes, recipe_detail, StoryListView, StoryDetailView, ContactView, \
    CreateStoryView, StoryUpdateView, StoryDeleteView, manage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('recipes/', recipes, name='recipes'),
    path('stories/', StoryListView.as_view(), name='stories'),
    path('create-story/', CreateStoryView.as_view(), name='create_story'),
    path('delete-story/<str:slug>/', StoryDeleteView.as_view(), name='delete_story'),
    path('update-story/<str:slug>/', StoryUpdateView.as_view(), name='update_story'),
    path('stories/<str:slug>/', StoryDetailView.as_view(), name='story_detail'),
    path('recipes/<str:slug>/', recipe_detail, name='recipe_detail'),
    path('manage/', manage, name='manage'),
]