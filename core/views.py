from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "core/index.html")
def about(request):
    return render(request, "core/about.html")
def inicio(request):
    return render(request, "core/inicio.html")
def portafolio(request):
    return render(request, "core/portfolio.html")

def contacto(request):
    return render(request, "core/contacto.html")