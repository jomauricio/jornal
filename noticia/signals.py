from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token



from .models import Autor

User = get_user_model()

@receiver(post_save, sender=User)  # add this
def create_user_autor(sender, instance, created, **kwargs):
    if created:
        Autor.objects.create(user=instance)
        Token.objects.create(user=instance)
