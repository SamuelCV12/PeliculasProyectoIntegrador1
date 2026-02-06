from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'name': 'Maria Laura Tafur'})
    #return HttpResponse('<h1>Welcome to the Movie Reviews Home Page!</h1>')
# Create your views here.
 #return render(request, 'home.html')
# el render localiza el archivo, procesa el html 
#y lo mete dentro de un Httpresponse que el mismo crea
# entrega ese paquete hacia el navegador del usuario