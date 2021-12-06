from django.contrib import admin

from .models import Author
from .models import Article

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title','author')
    list_filter = ('author',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
# Register your models here.
