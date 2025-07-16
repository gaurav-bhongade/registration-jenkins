# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash password
            user.save()
            return render(request, 'registration_success.html', {'user': user})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(username=uname, password=pwd)
            if user:
                login(request, user)  # Creates a session
                return render(request, 'welcome.html', {'user': user})  # Redirect to welcome page
            else:
                message = 'Invalid credentials'
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'message': message})


# accounts/views.py
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
