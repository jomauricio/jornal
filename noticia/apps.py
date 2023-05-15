from django.apps import AppConfig


class NoticiaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'noticia'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals