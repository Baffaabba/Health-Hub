from django.shortcuts import render, redirect, reverse
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

from .forms import SignUpForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        next = request.META.get('HTTP_REFERER', 'home')
        if next == "http://127.0.0.1:8000/login/":
            next = 'home'
        if form.is_valid():
            email = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=raw_password)
            if user is not None:
                print("Logging in")
                login(request, user)
                print(next)
                return redirect(next)
    else:
        form = AuthenticationForm()
        

    return render(request, 'registration/login.html', {'form': form})

def signup_view(request):

    if request.method=='POST':
        form = SignUpForm(request.POST)
        next = request.META.get('HTTP_REFERER', 'store')
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password')
            # user = authenticate(request, email=username, password=password)
            login(request, user)
            return redirect(next or 'store')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('store') 