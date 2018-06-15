from django.contrib.auth import login as django_login
from django.shortcuts import render, redirect

from member.forms import UserSignUpForm


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
