from django.shortcuts import render
from django.http import HttpResponse
from app_uno.models import Post, Comentarios
from app_uno.forms import Posteos_Form
# from mi_blog.app_uno.models import Pelicula


def index(request):

    return render( request , "index.html" )

def lecturas (request): 
    
    return render (request, "lecturas.html")

def peliculas (request): 
    
    return render (request, "peliculas.html")

def post (request): 
    
    return render (request, "post.html")

def posts (request): 
    lista_posts = Post.objects.all()
    posts = lista_posts
    return render (request, "lecturas.html", {"posts":posts })



# def eliminar_post(request,id):
#     post = Post.objects.get(id=id)
#     post.delete()
    
#     post = Post.objects.all()
    
#     return render(request, 'eliminar_post.html', {'mensaje':f"Post eliminado correctamente"})

def eliminar_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    
    post = Post.objects.all()

    return render(request , "lecturas.html" , {"lecturas": post})

    
    # return render(request, 'eliminar_post.html', {'mensaje':f"Post eliminado correctamente"})



def editar_post ( request , id):

    post = Post.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Posteos_Form( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            post.titulo = datos['titulo']
            post.contenido = datos['contenido']
            post.fecha = datos['fecha']
            post.nombre_libro = datos['nombre_libro']
            post.autor = datos['autor']
            post.lanzamiento = datos['lanzamiento']
            post.save()

            post = Post.objects.all()          
            return render(request , "lecturas.html" , {"lecturas": post})
        
    else:
        mi_formulario = Posteos_Form(initial={'titulo':post.titulo , "contenido":post.contenido, 'fecha':post.fecha, 'nombre_libro':post.nombre_libro, 'autor':post.autor, 'lanzamiento':post.lanzamiento})
        
    return render( request , "editar_post.html" , {"mi_formulario":mi_formulario, "post": post})







def alta_lecturas (request):

# llega el formulario, si viene con el metodo post, ingresa 
    if request.method == "POST":
        
# le paso a mi variable todos los datos que vienen en el form en este momento. Llamo a la clase Lecturas y le paso ese formulario. Ahora es un "formuñario django"
        form_lecturas = Posteos_Form( request.POST )
        
# si todo viene ok --> True. Cleaned_data es un diccionario que se ejecuta Solamente despues de "is valid". Cuando retorna T se genera el dicc con los datos del formulario limpios
        if form_lecturas.is_valid():
            datos = form_lecturas.cleaned_data          
            
            libro = Post( nombre=datos['nombre'] , autor=datos['autor'], año=datos['año'])
            libro.save()

            return render( request , "alta_lecturas.html")

    return render( request, "alta_lecturas.html")

    



def alta_post (request):

    if request.method == "POST":
        
        form_posteos = Posteos_Form( request.POST )
        
        if form_posteos.is_valid():
            datos = form_posteos.cleaned_data          
            
            posteo = Post ( titulo=datos['titulo'] , contenido=datos['contenido'], fecha=datos['fecha'], nombre_libro = datos['nombre_libro'], autor =datos['autor'], lanzamiento=datos['lanzamiento'])
            posteo.save()

            return render( request , "alta_post.html")

    return render( request, "alta_post.html")




def buscar_libro(request):

    return render( request , "buscar_libro.html")

def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        libros = Post.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"libros": libros})
    else:
        return HttpResponse("Campo vacio")