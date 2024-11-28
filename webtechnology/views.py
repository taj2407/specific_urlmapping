from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def trainer1(request):
    return HttpResponse('<h1>kishore sir teach javascript<h1>')
def trainer2(request):
    return HttpResponse('<h1>vicky sir teach webtechnology </h1>')