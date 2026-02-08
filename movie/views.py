from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie   


def home(request):
    #return render(request, 'home.html', {'name': 'Maria Laura Tafur Gomez'})
    searchTerm = request.GET.get('search')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
     movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})
    

def about(request):
    return render(request, 'about.html',)



#OJO: CADA PAGINA DEBE TENER SU FUNCION EN VIEWS DE RESPUESTA A LA URL QUE SE LE ASIGNE EN URLS.PY
    #return HttpResponse('<h1>Welcome to the Movie Reviews Home Page!</h1>')

#FUNCION DEL RENDER: 
# el render localiza el archivo, procesa el html 
#y lo mete dentro de un Httpresponse que el mismo crea
# entrega ese paquete hacia el navegador del usuario

#ABOUT PAGE:
 #Antes, se muestra un mensaje simple con HttpResponse.
   # return render(request, 'about.html') 
   # Después, se crea un archivo about.html en la carpeta templates 
   #y se llama a ese archivo desde la función about. De esta manera, 
   #se puede crear una página más completa y personalizada.