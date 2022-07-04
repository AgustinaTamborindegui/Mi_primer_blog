from django.shortcuts import render
from django.http import HttpResponse
# from Mi_primer_blog import app_unoc
from app_uno.models import Post, Comentarios, Avatar
from app_uno.forms import Posteos_Form, CreateUserForm, UserEditForm, ComentariosForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User



def index(request):
    return render( request , "index.html" )

def avatares(request):
    return render( request , "avatares.html" )

def lecturas (request): 
    return render (request, "lecturas.html")


def post (request): 
    return render (request, "post.html")

def posts (request): 
    lista_posts = Post.objects.all()
    posts = lista_posts
    return render (request, "lecturas.html", {"posts":posts })

 
@login_required
def eliminar_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    
    post = Post.objects.all()

    return render(request , "lecturas.html" , {"lecturas": post})

    



@login_required
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



def about_page(request):
    return render(request, 'About.html')



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

    


@login_required
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
    
    
    
    
def register(request):

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()
            return HttpResponse("Usuario creado")


    else:
        form = UserCreationForm()
    return render( request , "registro.html" , {"form":form})

# def registro(request):
#     if request.method == 'POST':
#         form = RegistroForm(request.POST)
        
#         if form.is_valid() :
#             form.save()
            
#             return render(request, 'index.html', {'mensaje':f"Usuario creado correctamente"})
#         else:
#             form=RegistroForm()
            
#             return render(request, 'registro.html', {'mensaje':f"Datos Incorrectos","form":form})
#     else:
#         form = RegistroForm()
    
    
    
    
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "inicio.html" ,{"url":avatares[0].imagen.url} )
                
                # lecturas = Post.objects.all()
                # return render(request, 'inicio.html', {'mensaje':f"Bienvenido/a {username}",'lecturas':lecturas})
            
            else:
                form=AuthenticationForm()
                return render(request, 'login.html', {'mensaje':f"Datos Incorrectos", "form":form})
        else:
            form=AuthenticationForm()
            return render(request, 'login.html', {'mensaje':f"Datos Incorrectos", "form":form})
        #revisar porque no me carga el ultimo form "form":form
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    

    
    
    
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render( request , "lecturas.html")

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render( request , "editar_perfil.html" , {"miFormulario":miFormulario , "usuario":usuario})



def comentar (request,id):
    post=Post.objects.get(id=id)
    comentarios = Comentarios.objects.filter(creado_en=post)
    
    crear_comentario=ComentariosForm(initial={'creado_por': request.user,'creado_en':post})
    if request.method == 'POST':
        crear_comentario=ComentariosForm(request.POST,initial={'creado_por': request.user,'creado_en':post})
        crear_comentario.save()
        return render(request, 'comentar.html', {'mensaje':f"Comentario creado correctamente","post":post,"comentarios":comentarios,"crear_comentario":crear_comentario})
    else:
        return render(request,'comentar.html',{'post':post,'comentarios':comentarios,'crear_comentario':crear_comentario})