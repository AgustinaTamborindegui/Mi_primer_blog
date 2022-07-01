from django import forms 
 
   
class Posteos_Form (forms.Form):
    titulo = forms.CharField(max_length=40)
    contenido = forms.CharField(max_length=2000)
    fecha = forms.DateField()
    nombre_libro = forms.CharField(max_length=40)
    autor = forms.CharField(max_length=40)
    lanzamiento = forms.DateField()
    





