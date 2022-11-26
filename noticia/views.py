from django.shortcuts import render, redirect, get_object_or_404
from .models import Noticia, Autor
from .forms import AutorForm, NoticiaForm

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

def listar_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, "listar_noticia.html", {"noticias": noticias})

def detalhar_noticia(request, id):
    noticia = Noticia.objects.get(id=id)
    return render(request, "detalhar_noticia.html", {"noticia": noticia})

def criar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            noticia = form.save()
            return redirect('/')
    else:
        form = NoticiaForm()
    return render(request, 'criar_noticia.html', {'form': form})

def atualizar_noticia(request, id):
    noticia = get_object_or_404(Noticia, pk=id)
    form = NoticiaForm(instance=noticia)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            noticia = form.save()
            return redirect('/')
        else:
            return render(request, 'atualizar_noticia.html', {'form': form, 'noticia': noticia})
    else:
        return render(request, 'atualizar_noticia.html', {'form': form, 'noticia': noticia})
        
def deletar_noticia(request, id):
    noticia = get_object_or_404(Noticia, pk=id)
    noticia.delete()
    return redirect('/')