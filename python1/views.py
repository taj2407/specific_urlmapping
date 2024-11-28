from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def harshad(request):
    return HttpResponse('<h1>harshad sir teach python and django</h1>')
def pranay(request):
    return HttpResponse('<h1>pranay sir also teach python</h1>')