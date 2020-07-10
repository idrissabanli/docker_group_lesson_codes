from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from accounts.forms import RegisterForm
from django.views.generic import ListView
from stories.models import Story, Recipe
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Istifadeci ugurla yaradildi')
            return redirect(reverse_lazy('home'))
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


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