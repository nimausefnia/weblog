from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserLoginForm, UserRegistrationForm


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            username = authenticate(request, username=username, password=password)
            if username is not None:
                login(request, username)
                messages.success(request, 'شما به درستی لاگین شدید', 'success')

                return redirect('blog:all_article')
            else:
                messages.error(request, 'login feiled', 'danger')

    else:
        form = UserLoginForm
        return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            messages.success(request, 'you registered successfully, now log in', 'success')
            return redirect('accounts:user_login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'loged ooout', 'success')
    return redirect('blog:all_article')
