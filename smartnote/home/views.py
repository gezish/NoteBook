from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/home.html',{})

@login_required
def authorized(request):
    return render(request, 'home/authorized.html',{})

@login_required(login_url='/admin')
def AboutMe(request):
    return render(request, 'home/AboutMe.html',{})