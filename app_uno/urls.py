from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name= "index"),
    path("posts", views.posts, name="lecturas"),
    path("post", views.post, name="post"),
    path("lecturas", views.posts, name="posts"),
    path("alta_lecturas", views.alta_lecturas, name="alta_lecturas"),
    path("alta_post", views.alta_post, name= "alta_post"),
    path('eliminar_post/<int:id>', views.eliminar_post, name="eliminar_post"),
    path('editar_post/<int:id>',views.editar_post,name="editar_post"),
    path('editar_post/',views.editar_post,name="editar_post"),
    path("buscar_libro", views.buscar_libro ),
    path("buscar", views.buscar),
    path("login" , views.login_request , name="login"),
    path("register", views.register, name="register"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="logout"),
    path("editarPerfil" , views.editarPerfil , name="editarPerfil"),
    path("avatares", views.avatares, name= "avatares")
   

    
]