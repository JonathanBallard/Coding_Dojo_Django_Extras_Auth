from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
from .forms import * 
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Create your views here. 
def index(request): 

    loginForm = AuthenticationForm
    registerForm = UserCreationForm(request.POST)
    myUserForm = UserForm
    context = {
        'registerForm' : registerForm,
        'loginForm' : loginForm,
        'userForm' : myUserForm,
    }


    return render(request, 'auth_app/index.html', context) 


def registerUser(request):
    loginForm = AuthenticationForm
    registerForm = UserCreationForm(request.POST)


    if registerForm.is_valid():
        user = registerForm.save()
    else:
        print('Form Invalid')
        return redirect('/')

    return redirect('/success/')


def loginUser(request):
    un = request.POST['username']
    pw = request.POST['password']

    testuser = authenticate(username=un, password=pw)
    if not testuser == None:
        login(request, testuser)
        return redirect('/success/')
    else:
        return redirect('/')


def success(request):
    allUsers = User.objects.all()
    thisUser = request.user

    thisUser.first_name = "jonathan"
    thisUser.save()


    context = {
        "all_users" : allUsers,
        'thisUser' : thisUser,


    }
    return render(request, 'auth_app/success.html', context)





def userFormRoute(request):
    pass






