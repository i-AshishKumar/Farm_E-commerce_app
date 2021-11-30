from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    return render(request,'home.html')
    
def products(request):
    item=Product.objects.all()
    return render(request,'products.html',{'item':item})

def cart(request):
    return render(request,'cart.html')