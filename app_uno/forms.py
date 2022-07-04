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
        
class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email' , 'password1' , 'password2']
        help_text = {k:"" for k in fields}

    





