from django.urls import path
from api.views import recipes_api, recipe, SubscriberCreateAPIView
from api.routers import router

urlpatterns = [
    path('recipes/', recipes_api, name='api_recipes'),
    path('recipes/<int:id>/', recipe, name='api_recipe'),
    path('subscribe/', SubscriberCreateAPIView.as_view(), name='subscribe'),
] + router.urls
