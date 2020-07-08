"""food_stories URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from stories.views import home, about, recipes, recipe_detail, StoryListView, StoryDetailView, ContactView, \
    CreateStoryView
from accounts.views import register

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('recipes/', recipes, name='recipes'),
    path('register/', register, name='register'),
    path('stories/', StoryListView.as_view(), name='stories'),
    path('create-story/', CreateStoryView.as_view(), name='create_story'),
    path('stories/<str:slug>/', StoryDetailView.as_view(), name='story_detail'),
    path('recipes/<str:slug>/', recipe_detail, name='recipe_detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
