from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def authDirect(request):
    return render(request,"Base/authenticate-direct.html")

def index(request):
    return render(request,"Base/index.html")

def LoginRegisterUser(request):
    page = "register"
    form = UserRegisterForm()

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

    return render(request , "Base/LoginRegisterUser.html",{"form":form})
