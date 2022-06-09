from django import forms 
 



    
class Posteos_Form (forms.Form):
    titulo = forms.CharField(max_length=40)
    contenido = forms.CharField(max_length=2000)
    fecha = forms.DateField()

class Lecturas_Form (forms.Form):
    nombre = forms.CharField(max_length=40)
    autor = forms.CharField(max_length=40)
    año = forms.DateField()

class Peliculas_Form (forms.Form):
    nombre = forms.CharField(max_length=40)
    año_estreno = forms.DateField()

