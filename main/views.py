from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def homes(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        name=request.POST.get('uname')
        password=request.POST.get('upassword')
        users = authenticate(request, name=name, password=password)
        if users is not None:
            login(request, users)
            return redirect('homes')
        else:
            return redirect('login')
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        name=request.POST.get('uusername')
        email=request.POST.get('uemail')
        password=request.POST.get('upassword')
        new_user = User.objects.create_user(username=name, email=email, password=password)
        new_user.save()
        return redirect('login')
    return render(request, 'signup.html')

def products(request):
    return render(request, 'products.html')


