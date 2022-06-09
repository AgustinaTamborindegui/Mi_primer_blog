from django.shortcuts import render
from django.http import HttpResponse
from app_uno.models import Pelicula, Post, Libro
from app_uno.forms import Lecturas_Form, Peliculas_Form, Posteos_Form
# from mi_blog.app_uno.models import Pelicula


def index(request):

    return render( request , "index.html" )

def lecturas (request): 
    
    return render (request, "lecturas.html")

def peliculas (request): 
    
    return render (request, "peliculas.html")

def post (request): 
    
    return render (request, "post.html")




def alta_lecturas (request):

# llega el formulario, si viene con el metodo post, ingresa 
    if request.method == "POST":
        
# le paso a mi variable todos los datos que vienen en el form en este momento. Llamo a la clase Lecturas y le paso ese formulario. Ahora es un "formuñario django"
        form_lecturas = Lecturas_Form( request.POST )
        
# si todo viene ok --> True. Cleaned_data es un diccionario que se ejecuta Solamente despues de "is valid". Cuando retorna T se genera el dicc con los datos del formulario limpios
        if form_lecturas.is_valid():
            datos = form_lecturas.cleaned_data          
            
            libro = Libro ( nombre=datos['nombre'] , autor=datos['autor'], año=datos['año'])
            libro.save()

            return render( request , "alta_lecturas.html")

    return render( request, "alta_lecturas.html")
    



def alta_post (request):

    if request.method == "POST":
        
        form_posteos = Posteos_Form( request.POST )
        
        if form_posteos.is_valid():
            datos = form_posteos.cleaned_data          
            
            posteo = Post ( titulo=datos['titulo'] , contenido=datos['contenido'], fecha=datos['fecha'])
            posteo.save()

            return render( request , "alta_post.html")

    return render( request, "alta_post.html")





def alta_peliculas (request):

    if request.method == "POST":
        
        form_peliculas = Peliculas_Form( request.POST )
        
        if form_peliculas.is_valid():
            datos = form_peliculas.cleaned_data          
            
            pelicula = Pelicula ( nombre=datos['nombre'] , año_estreno=datos['año_estreno'])
            pelicula.save()

            return render( request , "alta_peliculas.html")

    return render( request, "alta_peliculas.html")

def buscar_libro(request):

    return render( request , "buscar_libro.html")

def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        libros = Libro.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"libros": libros})
    else:
        return HttpResponse("Campo vacio")