from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('products/',views.products),
    path('cart/',views.cart),
    path('products/<str:p_name>/',views.landing),
]