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
            "all_products",
            "fecha"
        ]

    def create(self, validated_data):
        print("Guardamos la data de Electro")
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
        print("Guardamos la data de Fashion")
        pprint(validated_data)
        try:
            datosFashion = Fashion.objects.create(**validated_data)
        except Exception as e:
            print(e)
        return datosFashion


class DashboardSerializerHouseHome (serializers.ModelSerializer):
    class Meta:
        model = HouseHome
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
        print("Guardamos la data de HouseHome")
        pprint(validated_data)
        try:
            datosHouseHome = HouseHome.objects.create(**validated_data)
        except Exception as e:
            print(e)
        return datosHouseHome


class DashboardSerializerKids(serializers.ModelSerializer):
    class Meta:
        model = Kids
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
        print("Guardamos la data de Kids")
        pprint(validated_data)
        try:
            datosKids = Kids.objects.create(**validated_data)
        except Exception as e:
            print(e)
        return datosKids


class DashboardSerializerBeautyHealth(serializers.ModelSerializer):
    class Meta:
        model = BeautyHealth
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
        print("Guardamos la data de BeautyHealth")
        pprint(validated_data)
        try:
            datosBeautyHealth = BeautyHealth.objects.create(**validated_data)
        except Exception as e:
            print(e)
        return datosBeautyHealth
