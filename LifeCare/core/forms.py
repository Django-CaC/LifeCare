from django import forms
from django.core.exceptions import ValidationError

class ContactoForm (forms.Form):
    nombre = forms.CharField(label="Nombre de contacto", required=True)
    apellido = forms.CharField(label="Apellido de contacto", required=True)
    edad = forms.IntegerField(label="Edad")
    mail = forms.EmailField(label="Mail", required=True)
    mensaje = forms.CharField(widget=forms.Textarea)
    
    def clean_edad(self):
        if self.cleaned_data["edad"] < 18:
            raise ValidationError("El usuario debe ser mayor de edad")
        
    def clean(self):
        #Este if simula un usuario cargado en la BBDD
        if self.cleaned_data['nombre'] == 'Juan' and self.cleaned_data['apellido'] == 'Perez':
            raise ValidationError("El usuario juan Perez ya esta dado de alta")
        
        #Si el usuario no existe se da de alta
        
        return self.cleaned_data
    