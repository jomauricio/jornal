from django.db import models

class Author(models.Model):
    name = models.CharField('Nome', max_length=100)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Autor')
    title = models.CharField('Título', max_length=200)
    content = models.TextField('Conteúdo')
    pub_date = models.DateTimeField('Data de publicação')

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'

    def __str__(self):
        return self.title