from django.shortcuts import render
from django.http import HttpResponse
def func1(request):
    return HttpResponse("name:hp,cost:70000 ")
def func2(request):
    return HttpResponse("name:lenovo,cost:65000 ")
def func3(request):
    return HttpResponse("name:dell,cost:45000 ")
    


# Create your views here.
