from django.shortcuts import render
from .models import Noticia, Autor

# Create your views here.

def home(request):
    autores = Autor.objects.all()
    noticias = Noticia.objects.all()[:5]
    return render(request, "home.html", {"noticias": noticias, "autores": autores})

def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, "listar_autor.html", {"autores": autores})

def detalhar_autor(request, id):
    autor = Autor.objects.get(id=id)
    return render(request, "detalhar_autor.html", {"autor": autor})