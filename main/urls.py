from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('products/',views.products),
    path('cart/',views.cart),
    path('products/<str:p_name>/',views.landing),
    path('contact/',views.contact),
    path('about/',views.about),
    path('searchr/',views.search,name='search'),
]
