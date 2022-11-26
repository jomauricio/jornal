from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia, Autor
from .forms import AutorForm

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

def criar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save()
            return redirect('/')
    else:
        form = AutorForm()
    return render(request, 'criar_autor.html', {'form': form})

def atualizar_autor(request, id):
    autor = get_object_or_404(Autor, pk=id)
    form = AutorForm(instance=autor)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            autor = form.save()
            return redirect('/')
        else:
            return render(request, 'atualizar_autor.html', {'form': form, 'autor': autor})
    else:
        return render(request, 'atualizar_autor.html', {'form': form, 'autor': autor})
        
def deletar_autor(request, id):
    autor = get_object_or_404(Autor, pk=id)
    autor.delete()
    return redirect('/')