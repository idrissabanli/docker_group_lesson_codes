from django.shortcuts import render
from accounts.forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)