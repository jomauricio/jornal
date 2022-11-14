from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField("Nome", max_length=200)
    data_nascimento = models.DateField("Data de nascimento")
    endereco = models.CharField("Endereço", max_length=200)

    def __str__(self):
        return self.nome + " - " + self.endereco
    
    class Meta:
        verbose_name="Autor"
        verbose_name_plural="Autores"

class Noticia(models.Model):

    titulo = models.CharField("Titulo", max_length=200)
    conteudo = models.TextField("Conteudo")
    data_pub = models.DateField("Data de publicação")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + " - " + self.autor.nome