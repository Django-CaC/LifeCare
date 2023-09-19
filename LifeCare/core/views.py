
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    return render(request, "core/index.html", context)


def login(request):
    return render(request, "core/login.html")

def usuario_registrado(request, usuario_activo):

    return HttpResponse (f"<h1>Bienvenido a LifeCare {usuario_activo} </h1>")
