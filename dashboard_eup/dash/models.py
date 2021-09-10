from django.db import models

# Create your models here.
class Datos(models.Model):
	tienda = models.CharField(max_length=20,null=True)

	actualizar = models.IntegerField(null=True)
	sixpm_actualizar = models.IntegerField(null=True)
	amazon_actualizar = models.IntegerField(null=True)
	ebay_actualizar = models.IntegerField(null=True)
	footlocker_actualizar = models.IntegerField(null=True)
	nike_actualizar = models.IntegerField(null=True)
	zappos_actualizar = models.IntegerField(null=True)

	actualizados = models.IntegerField(null=True)
	sixpm_actualizados = models.IntegerField(null=True)
	amazon_actualizados = models.IntegerField(null=True)
	ebay_actualizados = models.IntegerField(null=True)
	footlocker_actualizados = models.IntegerField(null=True)
	nike_actualizados = models.IntegerField(null=True)
	zappos_actualizados = models.IntegerField(null=True)

	creados = models.IntegerField(null=True)
	sixpm_creados = models.IntegerField(null=True)
	amazon_creados = models.IntegerField(null=True)
	ebay_creados = models.IntegerField(null=True)
	footlocker_creados = models.IntegerField(null=True)
	nike_creados = models.IntegerField(null=True)
	zappos_creados = models.IntegerField(null=True)

	listos_subir_meli = models.IntegerField(null=True)
	listos_subir_zyte = models.IntegerField(null=True)