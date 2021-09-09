from django.db import models

# Create your models here.
class Datos(models.Model):
	tienda = tienda.CharField(max_length=20)
	dato = models.IntegerField()