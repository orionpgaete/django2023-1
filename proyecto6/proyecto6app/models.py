from django.db import models

# Create your models here.
class Proyecto(models.Model):
    fechaInicio = models.DateField()
    fechaTermino = models.DateField()
    nombre = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)
    prioriodad = models.IntegerField()

    