import pymongo
import requests
import json
from dash.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dash.models import Fashion, Kids, BeautyHealth, HouseHome, Electro


@api_view(['GET'])
def obtainAllData(request):
    cadenaFashion = 'http://ec2-3-137-143-15.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaKids = 'http://ec2-3-144-150-219.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaBeautyHealth = 'http://ec2-3-133-83-99.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaHouseHome = ''
    cadenaElectro = 'http://ec2-18-118-170-239.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'

    listaFashion = ConvertirLista(cadenaFashion)
    listaKids = ConvertirLista(cadenaKids)
    listaBeautyHealth = ConvertirLista(cadenaBeautyHealth)
    listaHouseHome = ConvertirLista(cadenaHouseHome)
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
    elif tienda == 'kids':
        ultimos = Kids.objects.all().order_by('-idKids')[:cantidad]
    elif tienda == 'beautyhealth':
        ultimos = BeautyHealth.objects.all().order_by('-idBeautyHealth')[:cantidad]
    elif tienda == 'househome':
        ultimos = HouseHome.objects.all().order_by('-idHouseHome')[:cantidad]
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
            
