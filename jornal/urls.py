"""jornal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from noticia.views import home, listar_autores, detalhar_autor, criar_autor, atualizar_autor, deletar_autor, listar_noticias, detalhar_noticia, criar_noticia, atualizar_noticia, deletar_noticia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('listar_autores/', listar_autores, name='listar_autores'),
    path('detalhar_autor/<int:id>/', detalhar_autor, name='detalhar_autor'),
    path('criar_autor/', criar_autor, name='criar_autor'),
    path('atualizar_autor/<int:id>/', atualizar_autor, name='atualizar_autor'),
    path('deletar_autor/<int:id>/', deletar_autor, name='deletar_autor'),
    path('listar_noticia/', listar_noticias, name='listar_noticias'),
    path('detalhar_noticia/<int:id>/', detalhar_noticia, name='detalhar_noticia'),
    path('criar_noticia/', criar_noticia, name='criar_noticia'),
    path('atualizar_noticia/<int:id>/', atualizar_noticia, name='atualizar_noticia'),
    path('deletar_noticia/<int:id>/', deletar_noticia, name='deletar_noticia'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
