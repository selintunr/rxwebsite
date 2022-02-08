from django.shortcuts import render

from django.http import HttpResponseRedirect

import requests

# Create your views here.


def index(request):
    return render(request, 'index.html')


def event(request):
    return render(request, 'event.html')    


def contact(request):
    return render(request, 'contact.html')        

def about(request):
    return render(request, 'about.html')            

def release(request):
    return render(request, 'release.html') 

def artist(request):
    return render(request, 'artist.html')         