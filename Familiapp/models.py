from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre= models.CharField(max_length=20)
    apellido= models.CharField(max_length=20)
    parentezco= models.CharField(max_length=20)
    edad= models.IntegerField()
    fechaNacimiento= models.DateField()
    