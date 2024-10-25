
from django.shortcuts import render
from django.http import HttpResponse
def func1(request):
    return HttpResponse("name:samsung,cost:20000 ")
def func2(request):
    return HttpResponse("name:vivo,cost:30000 ")
def func3(request):
    return HttpResponse("name:realme,cost:15000 ")
    

# Create your views here.
