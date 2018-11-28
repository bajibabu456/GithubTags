from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world(req):
    return HttpResponse("Hello World!")

def update_name(req):
    return HttpResponse('Name is updated successfully')
