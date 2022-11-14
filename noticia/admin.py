from django.contrib import admin
from .models import Autor, Noticia

# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    model=Autor

class NoticiaAdmin(admin.ModelAdmin):
    model=Noticia 

admin.site.register(Autor, AutorAdmin)
admin.site.register(Noticia, NoticiaAdmin)
