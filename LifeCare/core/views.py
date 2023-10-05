
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactoForm
from .models import Persona

# Create your views here.
def index(request):
    context = {}
    return render(request, "core/index.html", context)

def contacto(request):
    if request.method == 'POST':
        #Instanciamos un formulario con datos
        formulario = ContactoForm(request.POST)
        
        #Validarlo
        if formulario.is_valid():
            #Dar de alta la info
            
            messages.info(request, 'Consulta enviada con éxito')
            
            #Agregar los campos para dar de alta en la BBDD
            
                        
            return redirect(reverse('index'))
             
    else: #GET
        formulario = ContactoForm()
    
    context = {
        "contacto_form": formulario
    }
    return render(request,"core/contacto.html", context)


def login(request):
    return render(request, "core/login.html")

def usuario_registrado(request, usuario_activo):

    return HttpResponse (f"<h1>Bienvenido a LifeCare {usuario_activo} </h1>")
