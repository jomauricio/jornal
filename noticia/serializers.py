from dataclasses import fields
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedRelatedField
from .models import Noticia, Autor

class AutorModelSerializer(ModelSerializer):
    
    class Meta:
        model = Autor
        exclude = ["user"]


class NoticiaModelSerializer(ModelSerializer):

    class Meta:
        model = Noticia
        fields = "__all__"