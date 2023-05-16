from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Autor(models.Model):
    nome = models.CharField("Nome", max_length=200, blank=True)
    data_nascimento = models.DateField("Data de nascimento", blank=True, null=True)
    endereco = models.CharField("Endereço", max_length=200, blank=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.DO_NOTHING)

    def __str__(self):
        if self.nome:
            return self.nome + " - " + self.endereco
        else:
            return self.user.username
    
    class Meta:
        verbose_name="Autor"
        verbose_name_plural="Autores"

class Noticia(models.Model):

    titulo = models.CharField("Titulo", max_length=200)
    subtitulo = models.CharField("Subtitulo", max_length=200)
    conteudo = models.TextField("Conteudo")
    likes = models.SmallIntegerField("Likes", blank=True, null=True, default=0)
    data_pub = models.DateField("Data de publicação")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='noticias')

    def __str__(self):
        return self.titulo + " - " + self.autor.nome