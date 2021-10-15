import pymongo
import requests
import json
import datetime
from dash.models import *
from rest_framework.decorators import api_view
from dash.services import save_service


def obtainAllData():
    cadenaFashion = 'http://ec2-18-218-217-186.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaKids = 'http://ec2-18-117-168-228.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaBeautyHealth = 'http://ec2-18-218-117-226.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaHouseHome = 'http://ec2-18-117-219-250.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaElectro = 'http://ec2-18-118-170-239.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'

    listaFashion = ConvertirLista(cadenaFashion, "other")
    listaKids = ConvertirLista(cadenaKids, "other")
    listaBeautyHealth = ConvertirLista(cadenaBeautyHealth, "other")
    listaHouseHome = ConvertirLista(cadenaHouseHome, "other")
    listaElectro = ConvertirLista(cadenaElectro, "other")

    body_fashion = {
        "actualizar": listaFashion[0],
        "sixpm_actualizar": listaFashion[1],
        "amazon_actualizar": listaFashion[2],
        "ebay_actualizar": listaFashion[3],
        "footlocker_actualizar": listaFashion[4],
        "nike_actualizar": listaFashion[5],
        "zappos_actualizar": listaFashion[6],
        "actualizados": listaFashion[7],
        "sixpm_actualizados": listaFashion[8],
        "amazon_actualizados": listaFashion[9],
        "ebay_actualizados": listaFashion[10],
        "footlocker_actualizados": listaFashion[11],
        "nike_actualizados": listaFashion[12],
        "zappos_actualizados": listaFashion[13],
        "creados": listaFashion[14],
        "sixpm_creados": listaFashion[15],
        "amazon_creados": listaFashion[16],
        "ebay_creados": listaFashion[17],
        "footlocker_creados": listaFashion[18],
        "nike_creados": listaFashion[19],
        "zappos_creados": listaFashion[20],
        "listos_subir_meli": listaFashion[21],
        "listos_subir_zyte": listaFashion[22],
        "all_products": listaFashion[23],
        "fecha": datetime.datetime.now()
    }

    body_kids = {
        "actualizar": listaKids[0],
        "sixpm_actualizar": listaKids[1],
        "amazon_actualizar": listaKids[2],
        "ebay_actualizar": listaKids[3],
        "footlocker_actualizar": listaKids[4],
        "nike_actualizar": listaKids[5],
        "zappos_actualizar": listaKids[6],
        "actualizados": listaKids[7],
        "sixpm_actualizados": listaKids[8],
        "amazon_actualizados": listaKids[9],
        "ebay_actualizados": listaKids[10],
        "footlocker_actualizados": listaKids[11],
        "nike_actualizados": listaKids[12],
        "zappos_actualizados": listaKids[13],
        "creados": listaKids[14],
        "sixpm_creados": listaKids[15],
        "amazon_creados": listaKids[16],
        "ebay_creados": listaKids[17],
        "footlocker_creados": listaKids[18],
        "nike_creados": listaKids[19],
        "zappos_creados": listaKids[20],
        "listos_subir_meli": listaKids[21],
        "listos_subir_zyte": listaKids[22],
        "all_products": listaKids[23],
        "fecha": datetime.datetime.now()
    }
    body_beautyhealth = {
        "actualizar": listaBeautyHealth[0],
        "sixpm_actualizar": listaBeautyHealth[1],
        "amazon_actualizar": listaBeautyHealth[2],
        "ebay_actualizar": listaBeautyHealth[3],
        "footlocker_actualizar": listaBeautyHealth[4],
        "nike_actualizar": listaBeautyHealth[5],
        "zappos_actualizar": listaBeautyHealth[6],
        "actualizados": listaBeautyHealth[7],
        "sixpm_actualizados": listaBeautyHealth[8],
        "amazon_actualizados": listaBeautyHealth[9],
        "ebay_actualizados": listaBeautyHealth[10],
        "footlocker_actualizados": listaBeautyHealth[11],
        "nike_actualizados": listaBeautyHealth[12],
        "zappos_actualizados": listaBeautyHealth[13],
        "creados": listaBeautyHealth[14],
        "sixpm_creados": listaBeautyHealth[15],
        "amazon_creados": listaBeautyHealth[16],
        "ebay_creados": listaBeautyHealth[17],
        "footlocker_creados": listaBeautyHealth[18],
        "nike_creados": listaBeautyHealth[19],
        "zappos_creados": listaBeautyHealth[20],
        "listos_subir_meli": listaBeautyHealth[21],
        "listos_subir_zyte": listaBeautyHealth[22],
        "all_products": listaBeautyHealth[23],
        "fecha": datetime.datetime.now()
    }
    body_househome = {
        "actualizar": listaHouseHome[0],
        "sixpm_actualizar": listaHouseHome[1],
        "amazon_actualizar": listaHouseHome[2],
        "ebay_actualizar": listaHouseHome[3],
        "footlocker_actualizar": listaHouseHome[4],
        "nike_actualizar": listaHouseHome[5],
        "zappos_actualizar": listaHouseHome[6],
        "actualizados": listaHouseHome[7],
        "sixpm_actualizados": listaHouseHome[8],
        "amazon_actualizados": listaHouseHome[9],
        "ebay_actualizados": listaHouseHome[10],
        "footlocker_actualizados": listaHouseHome[11],
        "nike_actualizados": listaHouseHome[12],
        "zappos_actualizados": listaHouseHome[13],
        "creados": listaHouseHome[14],
        "sixpm_creados": listaHouseHome[15],
        "amazon_creados": listaHouseHome[16],
        "ebay_creados": listaHouseHome[17],
        "footlocker_creados": listaHouseHome[18],
        "nike_creados": listaHouseHome[19],
        "zappos_creados": listaHouseHome[20],
        "listos_subir_meli": listaHouseHome[21],
        "listos_subir_zyte": listaHouseHome[22],
        "all_products": listaHouseHome[23],
        "fecha": datetime.datetime.now()
    }
    body_electro = {
        "actualizar": listaElectro[0],
        "sixpm_actualizar": listaElectro[1],
        "amazon_actualizar": listaElectro[2],
        "ebay_actualizar": listaElectro[3],
        "footlocker_actualizar": listaElectro[4],
        "nike_actualizar": listaElectro[5],
        "zappos_actualizar": listaElectro[6],
        "actualizados": listaElectro[7],
        "sixpm_actualizados": listaElectro[8],
        "amazon_actualizados": listaElectro[9],
        "ebay_actualizados": listaElectro[10],
        "footlocker_actualizados": listaElectro[11],
        "nike_actualizados": listaElectro[12],
        "zappos_actualizados": listaElectro[13],
        "creados": listaElectro[14],
        "sixpm_creados": listaElectro[15],
        "amazon_creados": listaElectro[16],
        "ebay_creados": listaElectro[17],
        "footlocker_creados": listaElectro[18],
        "nike_creados": listaElectro[19],
        "zappos_creados": listaElectro[20],
        "listos_subir_meli": listaElectro[21],
        "listos_subir_zyte": listaElectro[22],
        "all_products": listaElectro[23],
        "fecha": datetime.datetime.now()
    }
    saveFashion = save_service.savedash(body_fashion, "fashion")
    saveElectro = save_service.savedash(body_electro, "electro")
    saveHouseHome = save_service.savedash(body_househome, "househome")
    saveBeautyHealth = save_service.savedash(body_beautyhealth, "beautyhealth")
    saveKids = save_service.savedash(body_kids, "kids")


def ConvertirLista(cadena, type_of_cadena):
    valores = []
    try:
        datoObtenido = requests.get(cadena)
        lista = datoObtenido.json()
        for llave in lista:
            valores.append(lista[llave])
    except Exception as e:
        if type_of_cadena == 'web':
            for i in range(24):
                valores.append('APAGADO')
        else:
            for i in range(24):
                valores.append(None)
    return valores
