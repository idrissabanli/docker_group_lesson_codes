from django.urls import path
from api.views import recipes_api, recipe

urlpatterns = [
    path('recipes/', recipes_api, name='api_recipes'),
    path('recipes/<int:id>/', recipe, name='api_recipe'),
]