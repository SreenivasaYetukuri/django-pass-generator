from re import T
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'password_generator/home.html')

def about(request):
    return render(request, 'password_generator/about.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    #
    # in below if conditions, the GET.get("?????") comes from the "name" in checkboxes from home.html
    #
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTVUWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    length= int(request.GET.get('length', 12))
    ## in top line "length" comes from the form select properties
    thepassword =''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'password_generator/password.html', {'password': thepassword})

def login(request):
    message="login sucessfull."
    return render(request, 'password_generator/login.html', { 'message': message} )