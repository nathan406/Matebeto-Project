from django.shortcuts import render,redirect
from .forms import CustomerSignUpForm,RestaurantOwnerSignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth

# Create your views here.

def authDirect(request):
    return render(request,"Base/authenticate-direct.html")

def index(request):
    return render(request,"Base/index.html")

def RegisterCustomer(request):
    # if page is register we will render the register form 
    page = "register"
    form = CustomerSignUpForm()

    context = {
        "page":page,
        "form":form,
    }

    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')

    return render(request , "Base/RegisterCustomer.html",{"context":context})

def LoginCustomer(request):
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

    return render(request, "Base/LoginCustomer.html" )


def RegisterRestaurantOwner(request):
    form = RestaurantOwnerSignUpForm()

    context = {
        "form":form,
    }

    if request.method == 'POST':
        form = RestaurantOwnerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')

    return render(request , "Base/RegisterRestaurantOwner.html",{"context":context})
    return render(request, "Base/RegisterRestaurant.html")

def LoginRestaurantOwner(request):
    if request.user.is_authenticated:
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
    return render(request, "Base/LoginRestaurantOwner.html")

def logout(request):
    auth.logout(request)
    return redirect('index')

def restaurantform(request):
    return render(request,"Base/restaurantform.html")