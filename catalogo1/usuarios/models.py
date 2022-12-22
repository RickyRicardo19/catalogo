from django.db import models 
from django.contrib.auth.models import AbstractBaseUser


class Usuario(AbstractBaseUser):
    es_administrador = models.BooleanField(default=False)