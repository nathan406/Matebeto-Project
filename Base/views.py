from django.shortcuts import render,redirect
from .forms import UserRegisterForm,RestaurantRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth

# Create your views here.

def authDirect(request):
    return render(request,"Base/authenticate-direct.html")

def index(request):
    return render(request,"Base/index.html")

def RegisterUser(request):
    # if page is register we will render the register form 
    page = "register"
    form = UserRegisterForm()

    context = {
        "page":page,
        "form":form,
    }

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')

    return render(request , "Base/RegisterUser.html",{"context":context})

def LoginUser(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    username = None
    password = None
    if request.method == 'POST':
        username = request.POST.get('username')
        if username is not None:
            username = username.lower()
        password = request.POST.get('password')
    
    user = authenticate(request,username=username , password=password)

    if user is not None:
        login(request,user)
        return redirect('index')

    return render(request, "Base/LoginUser.html" )

def RegisterRestaurant(request):
    form = RestaurantRegisterForm()

    context = {
        "form":form,
    }

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')

    return render(request , "Base/RegisterUser.html",{"context":context})
    return render(request, "Base/RegisterRestaurant.html")

def LoginRestaurant(request):
    if request.Resaturant.is_authenticated:
        return redirect('index')
    
    username = None
    password = None
    if request.method == 'POST':
        username = request.POST.get('username')
        if username is not None:
            username = username.lower()
        password = request.POST.get('password')
    
    Restaurant = authenticate(request,username=username , password=password)

    if Restaurant is not None:
        login(request,Restaurant)
        return redirect('index')
    return render(request, "Base/LoginRestaurant.html")

def logout(request):
    auth.logout(request)
    return redirect('index')