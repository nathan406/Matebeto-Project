from Base import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index ,name="index"),
    path("authDirect/",views.authDirect, name="authDirect"),
    path("RegisterUser/",views.RegisterUser , name="RegisterUser"),
    path('logout/', views.logout, name="logout"),
    path("LoginUser/",views.LoginUser, name="LoginUser"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)