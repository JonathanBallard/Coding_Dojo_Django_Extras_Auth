from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here. 
def index(request): 

    loginForm = AuthenticationForm
    registerForm = UserCreationForm(request.POST)

    context = {
        'registerForm' : registerForm,
        'loginForm' : loginForm,

    }


    return render(request, 'auth_app/index.html', context) 


def register(request):
    loginForm = AuthenticationForm
    registerForm = UserCreationForm(request.POST)

    print('registerForm.is_valid======================================================')
    print(registerForm.is_valid())
    if registerForm.is_valid():
        user = registerForm.save()
    else:
        print('-----------------------------------------------------------')
        print('Form Invalid')
        return redirect('/')
    
    print(registerForm.errors)

    return redirect('/success/')


def login(request):
    
    testuser = authenticate(username=request.POST['username'], password=request.POST['password'])

    if testuser != None:
        login(request, testuser)
        return redirect('/success/')
    else:
        print('-------------------------------------------------')
        print('Login Failed')
        return redirect('/')


def success(request):
    allUsers = User.objects.all()
    context = {
        "all_users" : allUsers,

    }

    return render(request, 'auth_app/success.html', context)












