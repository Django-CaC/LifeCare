from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}
    return render(request, "core/index.html", context)


def login(request):
    return render(request, "core/login.html")