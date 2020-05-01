from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")

def home(request):
    return HttpResponse("you are now on home")
