from django.db import models
from django.contrib.auth.models import User

class Post (models.Model):
    titulo = models.CharField(max_length=40)
    contenido = models.CharField(max_length=2000)
    fecha = models.DateField()
    nombre_libro = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    lanzamiento = models.DateField()
    
    def __str__(self):
        return self.titulo
    
class Comentarios(models.Model):
    comentario = models.TextField(max_length=500)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE,related_name='creado_por')
    creado = models.DateTimeField(auto_now_add=True)
    creado_en=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='creado_en')

    def __str__(self):
        return self.comentario
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares' , null=True , blank=True)
    

