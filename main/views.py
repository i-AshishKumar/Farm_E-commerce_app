from django.shortcuts import render
from .models import Product
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request,'home.html')
    
def products(request):
    item = Product.objects.all()
    return render(request,'products.html',{'item':item})

def cart(request):
    return render(request,'cart.html')

def landing(request,p_name):
    item = Product.objects.get(name=p_name)
    return render(request,'landing.html',{'item':item})

def contact(request):
    return render(request,'contact.html')

def search(request):
    if request.method == 'GET':
        srch = request.GET.get('q')
        results = Product.objects.all().filter(Q(name__icontains=srch) & Q(description__icontains=srch))
        return render(request,'search.html',{'results':results})

def about(request):
    return render(request,'about.html')