from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from users.forms import LoginForm, UserRegistrationForm
from users.models import SiteUser


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Успешная авторизация')
                else:
                    return HttpResponse('Аккаунт заблокирован')
            else:
                return HttpResponse('Неверный логин')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})
