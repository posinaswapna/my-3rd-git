from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def swapna(request):
    return HttpResponse('<h1>i m swapna</h1>')
def pavan(request):
    return HttpResponse('<h1>i m pavan</h1>')