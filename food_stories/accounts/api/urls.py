from django.urls import path
from accounts.api.views import register, CustomAuthToken
# from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api_account'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    
]