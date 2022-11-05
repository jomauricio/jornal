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