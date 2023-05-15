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
from noticia.views import Home, AutoresListView, AutorDetailView, NoticiaCreateView, RegistrationView, NoticiaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('news', NoticiaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('', include(router.urls)),
    path('noticias/', include('noticia.urls')),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('accounts/', include('django.contrib.auth.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
