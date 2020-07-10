from django.urls import path
from accounts.views import register, UserProfile


urlpatterns = [

    path('register/', register, name='register'),
    path('user-profile/', UserProfile.as_view(), name='user_profiel'),

]