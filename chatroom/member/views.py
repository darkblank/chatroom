from django.contrib.auth import login as django_login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from member.forms import UserSignUpForm, LoginForm


def signup(request):
    if request.method == 'POST':
        user_form = UserSignUpForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            django_login(request, user)
            return redirect('chat:index')
    else:
        user_form = UserSignUpForm()
    context = {
        'user_form': user_form
    }
    return render(request, 'member/signup.html', context)


def log_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            login_form.login(request)
            return redirect('chat:index')
        else:
            return HttpResponse('Login credential invalid')
    else:
        login_form = LoginForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'member/login.html', context)


@login_required
def log_out(request):
    logout(request)
    return redirect('chat:index')
