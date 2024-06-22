from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# LOGGING
def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('Main')
        else:
            messages.error(request, 'Wrong password or username!')
    return render(request, 'accounts/LoginUser.html')


def register_user(request):
    if request.method == "POST":
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        password = request.POST['password']

        if not User.objects.filter(username=email).exists():
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=email,
                email=email,
                password=password,
            )

            login(request, user)
            return redirect('Main')
        else:
            messages.error(request,
                           'A user with the same name already exists!\n'
                           'The name must be unique!')
    return render(request, 'accounts/RegisterUser.html')


def logout_user(request):
    logout(request)
    return redirect('Main')
