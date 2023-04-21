from django.db import models

class Opinion(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    libro = models.CharField(max_length=100)
    opinion = models.TextField()
# Create your models here.
