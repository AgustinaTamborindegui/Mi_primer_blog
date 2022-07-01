from unicodedata import name
from django.urls import path
from . import views

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
    path("buscar", views.buscar)

    
]