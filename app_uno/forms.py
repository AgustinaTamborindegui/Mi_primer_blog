from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
   
class Posteos_Form (forms.Form):
    titulo = forms.CharField(max_length=40)
    contenido = forms.CharField(max_length=2000)
    fecha = forms.DateField()
    nombre_libro = forms.CharField(max_length=40)
    autor = forms.CharField(max_length=40)
    lanzamiento = forms.DateField()
    
    
        


class CreateUserForm(UserCreationForm):

    email = forms.EmailField(label="email")
    

    class Meta:
        model=User
        fields=['email','username','password2']
        help_text={k:"" for k in fields}

    





