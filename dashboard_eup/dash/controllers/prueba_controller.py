import pymongo
import requests
import json
import datetime
from dash.models import *
from rest_framework.decorators import api_view
from dash.services import save_service


@api_view(['GET'])
def obtainAllData(request):
    cadenaFashion = 'http://ec2-18-222-217-205.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaKid = 'http://ec2-3-136-157-90.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaPets = 'http://ec2-3-22-61-127.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaHouseful = ''
    cadenaElectro = 'http://ec2-3-139-57-54.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'

    listaFashion = ConvertirLista(cadenaFashion, "other")
    listaKid = ConvertirLista(cadenaKid, "other")
    listaPets = ConvertirLista(cadenaPets, "other")
    listaHouseful = ConvertirLista(cadenaHouseful, "other")
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
        "fecha": datetime.datetime.now()
    }

    body_kid = {
        "actualizar": listaKid[0],
        "sixpm_actualizar": listaKid[1],
        "amazon_actualizar": listaKid[2],
        "ebay_actualizar": listaKid[3],
        "footlocker_actualizar": listaKid[4],
        "nike_actualizar": listaKid[5],
        "zappos_actualizar": listaKid[6],
        "actualizados": listaKid[7],
        "sixpm_actualizados": listaKid[8],
        "amazon_actualizados": listaKid[9],
        "ebay_actualizados": listaKid[10],
        "footlocker_actualizados": listaKid[11],
        "nike_actualizados": listaKid[12],
        "zappos_actualizados": listaKid[13],
        "creados": listaKid[14],
        "sixpm_creados": listaKid[15],
        "amazon_creados": listaKid[16],
        "ebay_creados": listaKid[17],
        "footlocker_creados": listaKid[18],
        "nike_creados": listaKid[19],
        "zappos_creados": listaKid[20],
        "listos_subir_meli": listaKid[21],
        "listos_subir_zyte": listaKid[22],
        "fecha": datetime.datetime.now()
    }
    body_pets = {
        "actualizar": listaPets[0],
        "sixpm_actualizar": listaPets[1],
        "amazon_actualizar": listaPets[2],
        "ebay_actualizar": listaPets[3],
        "footlocker_actualizar": listaPets[4],
        "nike_actualizar": listaPets[5],
        "zappos_actualizar": listaPets[6],
        "actualizados": listaPets[7],
        "sixpm_actualizados": listaPets[8],
        "amazon_actualizados": listaPets[9],
        "ebay_actualizados": listaPets[10],
        "footlocker_actualizados": listaPets[11],
        "nike_actualizados": listaPets[12],
        "zappos_actualizados": listaPets[13],
        "creados": listaPets[14],
        "sixpm_creados": listaPets[15],
        "amazon_creados": listaPets[16],
        "ebay_creados": listaPets[17],
        "footlocker_creados": listaPets[18],
        "nike_creados": listaPets[19],
        "zappos_creados": listaPets[20],
        "listos_subir_meli": listaPets[21],
        "listos_subir_zyte": listaPets[22],
        "fecha": datetime.datetime.now()
    }
    body_houseful = {
        "actualizar": listaHouseful[0],
        "sixpm_actualizar": listaHouseful[1],
        "amazon_actualizar": listaHouseful[2],
        "ebay_actualizar": listaHouseful[3],
        "footlocker_actualizar": listaHouseful[4],
        "nike_actualizar": listaHouseful[5],
        "zappos_actualizar": listaHouseful[6],
        "actualizados": listaHouseful[7],
        "sixpm_actualizados": listaHouseful[8],
        "amazon_actualizados": listaHouseful[9],
        "ebay_actualizados": listaHouseful[10],
        "footlocker_actualizados": listaHouseful[11],
        "nike_actualizados": listaHouseful[12],
        "zappos_actualizados": listaHouseful[13],
        "creados": listaHouseful[14],
        "sixpm_creados": listaHouseful[15],
        "amazon_creados": listaHouseful[16],
        "ebay_creados": listaHouseful[17],
        "footlocker_creados": listaHouseful[18],
        "nike_creados": listaHouseful[19],
        "zappos_creados": listaHouseful[20],
        "listos_subir_meli": listaHouseful[21],
        "listos_subir_zyte": listaHouseful[22],
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
        "fecha": datetime.datetime.now()
    }
    saveFashion = save_service.savedash(body_fashion, "fashion")
    saveElectro = save_service.savedash(body_electro, "electro")
    saveHouseful = save_service.savedash(body_houseful, "houseful")
    savePets = save_service.savedash(body_pets, "pets")
    saveKid = save_service.savedash(body_kid, "kid")


def ConvertirLista(cadena, type_of_cadena):
    valores = []
    try:
        datoObtenido = requests.get(cadena)
        lista = datoObtenido.json()
        for llave in lista:
            valores.append(lista[llave])
    except Exception as e:
        if type_of_cadena == 'web':
            for i in range(23):
                valores.append('APAGADO')
        else:
            for i in range(23):
                valores.append(None)
    return valores
