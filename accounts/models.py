from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#nuevo modelo de usuario que aplio o complementa el AbstractUser ya existente este contiene los siguienetes atributos
"""
username, first_name,  last_name, email, password, groups, user_permissions, is_staff, is_active,  
is_superuser, last_login y date_joined 
"""
class CustomUser(AbstractUser):
    #campos personalisados, edad y imagen de usuario
    age = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='imagenes_user/',default='static/img/user.png')
