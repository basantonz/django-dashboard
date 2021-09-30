import pymongo
import requests
import json
from dash.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dash.models import Fashion, Kid, Pets, Houseful, Electro


@api_view(['GET'])
def obtainAllData(request):
    cadenaFashion = 'http://ec2-3-137-143-15.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaKid = 'http://ec2-3-144-150-219.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaPets = 'http://ec2-3-133-83-99.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaHouseful = ''
    cadenaElectro = 'http://ec2-18-118-170-239.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'

    listaFashion = ConvertirLista(cadenaFashion)
    listaKid = ConvertirLista(cadenaKid)
    listaPets = ConvertirLista(cadenaPets)
    listaHouseful = ConvertirLista(cadenaHouseful)
    listaElectro = ConvertirLista(cadenaElectro)
    return Response('Todo ok')


def ConvertirLista(cadena, type_of_cadena):
    valores = []
    try:
        datoObtenido = requests.get(cadena)
        lista = datoObtenido.json()
        for llave in lista:
            valores.append(lista[llave])
            print(lista[llave])
    except Exception as e:
        if type_of_cadena == 'web':
            for i in range(24):
                valores.append('APAGADO')
        if type_of_cadena == 'grafica':
            for i in range(24):
                valores.append(0)
    return valores

def ConvertirLista2(tienda,cantidad):
    arregglo=[]
    arregglo_arreggladdo=[]
    if tienda == 'fashion':
        ultimos = Fashion.objects.all().order_by('-idFashion')[:cantidad]
    elif tienda == 'kid':
        ultimos = Kid.objects.all().order_by('-idKid')[:cantidad]
    elif tienda == 'pets':
        ultimos = Pets.objects.all().order_by('-idPets')[:cantidad]
    elif tienda == 'houseful':
        ultimos = Houseful.objects.all().order_by('-idHouseful')[:cantidad]
    elif tienda == 'electro':
        ultimos = Electro.objects.all().order_by('-idElectro')[:cantidad]
    for x in reversed(ultimos):
        arregglo.append(x.actualizar)
        arregglo.append(x.sixpm_actualizar)
        arregglo.append(x.amazon_actualizar)
        arregglo.append(x.ebay_actualizar)
        arregglo.append(x.footlocker_actualizar)
        arregglo.append(x.nike_actualizar)
        arregglo.append(x.zappos_actualizar)
        arregglo.append(x.actualizados)
        arregglo.append(x.sixpm_actualizados)
        arregglo.append(x.amazon_actualizados)
        arregglo.append(x.ebay_actualizados)
        arregglo.append(x.footlocker_actualizados)
        arregglo.append(x.nike_actualizados)
        arregglo.append(x.zappos_actualizados)
        arregglo.append(x.creados)
        arregglo.append(x.sixpm_creados)
        arregglo.append(x.amazon_creados)
        arregglo.append(x.ebay_creados)
        arregglo.append(x.footlocker_creados)
        arregglo.append(x.nike_creados)
        arregglo.append(x.zappos_creados)
        arregglo.append(x.listos_subir_meli)
        arregglo.append(x.listos_subir_zyte)
        arregglo.append(x.all_products)
    for x in arregglo:
        if x is None:
            arregglo_arreggladdo.append(0)
        else:
            arregglo_arreggladdo.append(x)
    return arregglo_arreggladdo
            
