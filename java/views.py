from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def ravi(request):
    return HttpResponse('<h1>ravi sir teach java course </h1>')
def bharath(request):
    return HttpResponse('<h1>bharath explain java very will</h1>')