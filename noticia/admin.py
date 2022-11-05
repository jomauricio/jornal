from django.contrib import admin
from .models import Autor

# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    model=Autor

admin.site.register(Autor, AutorAdmin)
