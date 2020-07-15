from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib import messages
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, \
    PasswordResetConfirmView
from accounts.tasks import send_confirmation_email
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, Group
from accounts.tools.token import account_activation_token

from stories.models import Story, Recipe, SavedArticle
from accounts.forms import CustomUserCreationForm, LoginForm, CustomPasswordChangeForm, CustomPasswordResetForm, ResetPasswordForm


User = get_user_model()


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Password set olundu')
        return super().form_valid(form)


class ForgetPasswordView(PasswordResetView):
    email_template_name = 'email/password_reset_email.html'
    template_name = 'forget_password.html'
    success_url = reverse_lazy('login')
    form_class = CustomPasswordResetForm

    def form_valid(self, form):
        messages.success(self.request, 'password deyisilmesi ucun sizin mail-e mesaj gonderildi!')
        return super().form_valid(form)

    
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset_password.html'
    success_url = reverse_lazy('login')
    form_class = ResetPasswordForm

    def form_valid(self, form):
        messages.success(self.request, 'password deyisdirildi')
        return super().form_valid(form)


# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, email=email, password=password)
#             if user:
#                 auth_login(request, user)
#                 messages.success(request, 'Ugurla Login olundu')
#                 return redirect(reverse_lazy('user_profile'))
#             else:
#                 messages.error(request, 'Bele bir user movcud deyil')
#     else:
#         form = LoginForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'login.html', context)

# def logout(request):
#     auth_logout(request)
#     return redirect(reverse_lazy('home'))

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False

            if form.cleaned_data.get('is_author') == 'write':
                group = Group.objects.get(name='author')
            else:
                group = Group.objects.get(name='reader')

            # if form.cleaned_data.get('is_author') == 'write':
            #     permission = Permission.objects.get(codename='add_recipe')
            # else:
            #     permission = Permission.objects.get(codename='view_recipe')
            user.save()
            saved_articles = request.COOKIES.get('saved_articles')
            if saved_articles:
                print(saved_articles)
                for saved_article_id in saved_articles.split(';'):
                    if saved_article_id and saved_article_id != '':
                        recipe = Recipe.objects.get(pk=int(saved_article_id))
                        SavedArticle.objects.get_or_create(user=user, recipe=recipe)
                request.COOKIES['saved_articles'] = ''
            user.groups.add(group)
            # user.user_permissions.add(permission)
            site_address = get_current_site(request).domain
            send_confirmation_email(user.id, site_address)
            # user = form.save(commit=False)
            # user.set_password(form.cleaned_data.get('password'))
            # user.save()
            messages.success(request, 'Istifadeci ugurla yaradildi, Zehmet olmasa Email-e daxil olub hesabinizi tesdiqleyin')
            return redirect(reverse_lazy('home'))
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
    messages.error('Activation link is invalid!')    
    return redirect('home')
    


class UserProfile(LoginRequiredMixin, ListView):
    model = Story
    template_name = 'user-profile.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user, is_published=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['recipes'] = Recipe.objects.filter(author=self.request.user, is_published=True)
        return context


