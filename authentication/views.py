from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})


def login(request):
    return render(request,'login.html')

def logoutView(request):
    logout(request)
    return redirect('/')

def profileView(request):
    return render(request,'profile.html')

