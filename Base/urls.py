from Base import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index ,name="index"),
    path("authDirect/",views.authDirect, name="authDirect"),
    path("RegisterCustomer/",views.RegisterCustomer , name="RegisterCustomer"),
    path('logout/', views.logout, name="logout"),
    path("LoginCustomer/",views.LoginCustomer, name="LoginCustomer"),
    path("LoginRestaurantOwner/",views.LoginRestaurantOwner, name="LoginRestaurantOwner" ),
    path("RegisterRestaurantOwner/",views.RegisterRestaurantOwner,name="RegisterRestaurantOwner"),
    path('restaurantform/', views.restaurantform, name="restaurantform")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)