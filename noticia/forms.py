from django.forms import ModelForm
from .models import Autor, Noticia

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'data_nascimento', 'endereco']

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'subtitulo', 'conteudo', 'data_pub', 'autor']

