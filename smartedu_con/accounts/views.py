from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . forms import LoginForm, RegisterForm

# Create your views here.

def user_login(request):
    if request == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

                else:
                    messages.info(request, 'Your account is not active')

            else:
                messages.info(request, 'Check your username and password')

    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})

def user_register(request):
    return render(request, 'register.html')

def user_logout(request):
    pass

def user_dashboard(request):
    pass
