from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   # return HttpResponse('<h1>Welcome to Home Page</h1>')
   #return render(request, 'home.html')
   return render(request, 'home.html', {'name':'Samuel Correa Velasquez'})

def about(request):
    return HttpResponse('<h1>Welcome to about Page</h1>')
