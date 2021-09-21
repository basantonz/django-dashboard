from django.db import models
from django.db.models.fields import AutoField

# Create your models here.


class Electro(models.Model):
    idElectro = models.AutoField(AutoField, primary_key=True)
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
    fecha = models.DateTimeField(null=True)

    class meta:
        db_table = 'Electro'


class Fashion(models.Model):
    idFashion = models.AutoField(primary_key=True)
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
    fecha = models.DateTimeField(auto_now_add=True)

    class meta:
        db_table = 'Fashion'


class Houseful(models.Model):
    idHouseful = models.AutoField(primary_key=True)
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
    fecha = models.DateTimeField(auto_now_add=True)

    class meta:
        db_table = 'Houseful'


class Kid(models.Model):
    idKid = models.AutoField(primary_key=True)
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
    fecha = models.DateTimeField(auto_now_add=True)

    class meta:
        db_table = 'Kid'


class Pets(models.Model):
    idPets = models.AutoField(primary_key=True)
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
    fecha = models.DateTimeField(auto_now_add=True)

    class meta:
        db_table = 'Pets'
