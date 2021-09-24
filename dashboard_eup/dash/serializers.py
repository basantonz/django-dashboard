from rest_framework import serializers
from django.conf import settings
from .models import *
from pprint import pprint


class DashboardSerializerElectro(serializers.ModelSerializer):
    class Meta:
        model = Electro
        fields = [
            "actualizar",
            "sixpm_actualizar",
            "amazon_actualizar",
            "ebay_actualizar",
            "footlocker_actualizar",
            "nike_actualizar",
            "zappos_actualizar",
            "actualizados",
            "sixpm_actualizados",
            "amazon_actualizados",
            "ebay_actualizados",
            "footlocker_actualizados",
            "nike_actualizados",
            "zappos_actualizados",
            "creados",
            "sixpm_creados",
            "amazon_creados",
            "ebay_creados",
            "footlocker_creados",
            "nike_creados",
            "zappos_creados",
            "listos_subir_meli",
            "listos_subir_zyte",
            "fecha"
        ]

    def create(self, validated_data):
        print("Guardamos la data")
        pprint(validated_data)
        try:
            datosElectro = Electro.objects.create(**validated_data)
        except Exception as e:
            print(e)
        return datosElectro


class DashboardSerializerFashion(serializers.ModelSerializer):
    class Meta:
        model = Fashion
        fields = [
            "actualizar",
            "sixpm_actualizar",
            "amazon_actualizar",
            "ebay_actualizar",
            "footlocker_actualizar",
            "nike_actualizar",
            "zappos_actualizar",
            "actualizados",
            "sixpm_actualizados",
            "amazon_actualizados",
            "ebay_actualizados",
            "footlocker_actualizados",
            "nike_actualizados",
            "zappos_actualizados",
            "creados",
            "sixpm_creados",
            "amazon_creados",
            "ebay_creados",
            "footlocker_creados",
            "nike_creados",
            "zappos_creados",
            "listos_subir_meli",
            "listos_subir_zyte",
            "all_products",
            "fecha"
        ]

    def create(self, validated_data):
        print("Guardamos la data")
        pprint(validated_data)
        try:
            datosFashion = Fashion.objects.create(**validated_data)
        except Exception as e:
            print(e)
        return datosFashion


class DashboardSerializerHouseful (serializers.ModelSerializer):
    class Meta:
        model = Houseful
        fields = [
            "actualizar",
            "sixpm_actualizar",
            "amazon_actualizar",
            "ebay_actualizar",
            "footlocker_actualizar",
            "nike_actualizar",
            "zappos_actualizar",
            "actualizados",
            "sixpm_actualizados",
            "amazon_actualizados",
            "ebay_actualizados",
            "footlocker_actualizados",
            "nike_actualizados",
            "zappos_actualizados",
            "creados",
            "sixpm_creados",
            "amazon_creados",
            "ebay_creados",
            "footlocker_creados",
            "nike_creados",
            "zappos_creados",
            "listos_subir_meli",
            "listos_subir_zyte",
            "all_products",
            "fecha"
        ]

    def create(self, validated_data):
        print("Guardamos la data")
        pprint(validated_data)
        try:
            datosHouseful = Houseful.objects.create(**validated_data)
        except Exception as e:
            print(e)
        return datosHouseful


class DashboardSerializerKid(serializers.ModelSerializer):
    class Meta:
        model = Kid
        fields = [
            "actualizar",
            "sixpm_actualizar",
            "amazon_actualizar",
            "ebay_actualizar",
            "footlocker_actualizar",
            "nike_actualizar",
            "zappos_actualizar",
            "actualizados",
            "sixpm_actualizados",
            "amazon_actualizados",
            "ebay_actualizados",
            "footlocker_actualizados",
            "nike_actualizados",
            "zappos_actualizados",
            "creados",
            "sixpm_creados",
            "amazon_creados",
            "ebay_creados",
            "footlocker_creados",
            "nike_creados",
            "zappos_creados",
            "listos_subir_meli",
            "listos_subir_zyte",
            "all_products",
            "fecha"
        ]

    def create(self, validated_data):
        print("Guardamos la data")
        pprint(validated_data)
        try:
            datosKid = Kid.objects.create(**validated_data)
        except Exception as e:
            print(e)
        return datosKid


class DashboardSerializerPets(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = [
            "actualizar",
            "sixpm_actualizar",
            "amazon_actualizar",
            "ebay_actualizar",
            "footlocker_actualizar",
            "nike_actualizar",
            "zappos_actualizar",
            "actualizados",
            "sixpm_actualizados",
            "amazon_actualizados",
            "ebay_actualizados",
            "footlocker_actualizados",
            "nike_actualizados",
            "zappos_actualizados",
            "creados",
            "sixpm_creados",
            "amazon_creados",
            "ebay_creados",
            "footlocker_creados",
            "nike_creados",
            "zappos_creados",
            "listos_subir_meli",
            "listos_subir_zyte",
            "all_products",
            "fecha"
        ]

    def create(self, validated_data):
        print("Guardamos la data")
        pprint(validated_data)
        try:
            datosPets = Pets.objects.create(**validated_data)
        except Exception as e:
            print(e)
        return datosPets
