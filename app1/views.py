from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>this is my project</h1>')
def second(request):
    return  HttpResponse('<h1>this is my 2nd project</h1>')