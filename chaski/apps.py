from django.apps import AppConfig


class ChaskiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chaski'

    def ready(self):
        import chaski.signals 
