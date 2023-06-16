from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=25)

# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
    
#     pass
