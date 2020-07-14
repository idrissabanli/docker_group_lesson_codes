from django.urls import path, re_path
from accounts.views import register, UserProfile, CustomLoginView, activate, CustomPasswordChangeView, \
    ForgetPasswordView, CustomPasswordResetConfirmView
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    re_path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate, name='activation'),
    re_path(r'password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('forget-password/', ForgetPasswordView.as_view(), name='forget_password'),
    path('user-profile/', UserProfile.as_view(), name='user_profile'),

]