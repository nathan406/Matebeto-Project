from Base import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index ,name="home"),
    path("authDirect/",views.authDirect, name="authDirect"),
    path("LoginRegister/",views.LoginRegisterUser , name="LoginRegisterUser")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)