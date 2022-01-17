from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Usuario

@receiver(post_save, sender= User )
def create_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)

@receiver(post_save, sender= User )
def save_usuario(sender, instance, **kwargs):
    instance.usuario.save()