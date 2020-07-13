from django.urls import path, re_path
from accounts.views import register, UserProfile, CustomLoginView, activate
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    re_path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate, name='activation'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user-profile/', UserProfile.as_view(), name='user_profile'),

]