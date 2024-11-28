from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def trainer1(request):
    return HttpResponse('<h1>jyoshna mam teach sql<h1>')
def trainer2(request):
    return HttpResponse('<h1> greeshma mam teach sql </h1>')