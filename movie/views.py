from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
     # HttpResponse("Welcome to the Movie/h1")

    return render(request, 'home.html', {'name': 'Greg Liam'})