from django.contrib.auth import login
from django.db import models
from django.contrib.auth.models import User 

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    

    def __str__(self):
        return f'{self.user.username}'


