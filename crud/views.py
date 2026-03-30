from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # Simple text response for root URL
    return HttpResponse("Welcome to the Django CRUD App!")
    
   