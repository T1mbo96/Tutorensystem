from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import SignUpForm


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def profile(request):
    return render(request, 'accounts/profile.html')
