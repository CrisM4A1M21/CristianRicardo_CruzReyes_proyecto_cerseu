from django.db import models

# Create your models here.


class Meseros(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=20)
    edad = models.IntegerField(default=0)
    procedencia = models.CharField(default='', max_length=20)


