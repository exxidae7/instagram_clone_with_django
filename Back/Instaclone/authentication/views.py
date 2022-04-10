from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login ,authenticate
from django.contrib.auth.forms import UserCreationForm
    
# Create your views here.


def index(response):
    return render(response , 'index.html')


def login(response):
    return render(response , 'login.html')
def signup(response):
    return render(response , 'signup.html')