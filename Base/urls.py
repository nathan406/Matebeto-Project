from Base import views
from django.urls import path

urlpatterns = [
    path("",views.index ,name="home"),
    path("authDirect/",views.authDirect, name="authDirect"),
    path("LoginRegister/",views.LoginRegisterUser , name="LoginRegisterUser")
]