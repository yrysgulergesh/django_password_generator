from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(reguest):
    return render(reguest, 'generator/home.html')

def about(reguest):
    return render(reguest, 'generator/about.html')

def password(reguest):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if reguest.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if reguest.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    
    if reguest.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(reguest.GET.get('length',10))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(reguest, 'generator/password.html', {'password':thepassword})