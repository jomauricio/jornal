from tkinter.font import families
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Noticia, Autor
from .forms import AutorForm, NoticiaForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework.views import APIView
from .serializers import NoticiaModelSerializer, AutorModelSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework import viewsets


# Create your views here.

def home(request):
    autores = Autor.objects.all()
    noticias = Noticia.objects.all()[:5]
    return render(request, "home.html", {"noticias": noticias, "autores": autores})

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["noticias"] = Noticia.objects.all()[:5]
        context["autores"] = Autor.objects.all()[:5]
        return context

def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, "listar_autor.html", {"autores": autores})

class AutoresListView(ListView):
    model = Autor
    template_name = "listar_autor.html"
    context_object_name = "autores"

def detalhar_autor(request, id):
    autor = Autor.objects.get(id=id)
    return render(request, "detalhar_autor.html", {"autor": autor})

class AutorDetailView(DetailView):
    model = Autor
    template_name =  "detalhar_autor.html"
    context_object_name = "autor"
    pk_url_kwarg = 'id'

@login_required
def criar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save()
            return redirect('/')
    else:
        form = AutorForm()
    return render(request, 'criar_autor.html', {'form': form})

@login_required
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

@login_required        
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

@login_required
def criar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            noticia = form.save()
            return redirect('/')
    else:
        form = NoticiaForm()
    return render(request, 'criar_noticia.html', {'form': form})

class NoticiaCreateView(LoginRequiredMixin, CreateView):
    template_name = 'criar_noticia.html'
    model = Noticia
    form_class = NoticiaForm
    success_url = "/"
    # fields = ['titulo', 'subtitulo', 'conteudo', 'data_pub', 'autor']


@login_required
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

@login_required        
def deletar_noticia(request, id):
    noticia = get_object_or_404(Noticia, pk=id)
    noticia.delete()
    return redirect('/')

def dar_like(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    if request.method == 'GET':
        noticia.likes += 1
        noticia.save()
        return redirect(reverse_lazy("detalhar_noticia", args=[noticia.pk]))
    else:
        return redirect(reverse_lazy("detalhar_noticia", args=[noticia.pk]))

class RegistrationView(CreateView):
    template_name = "registration/registration.html"
    model = User
    form_class = UserCreationForm
    success_url = "/"

class NoticiaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Noticia.objects.all()
    serializer_class = NoticiaModelSerializer

    @action(methods=['get'], detail=True)
    def likes(self, request, pk=None):
        noticia = get_object_or_404(Noticia, pk=pk)
        noticia.likes += 1
        noticia.save()

        return Response(NoticiaModelSerializer(noticia, many=False).data)

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorModelSerializer

