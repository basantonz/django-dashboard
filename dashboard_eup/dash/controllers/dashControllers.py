import pymongo
import requests
import json
from dash.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def obtainAllData(request):
    cadenaFashion = 'http://ec2-18-222-217-205.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaKid = 'http://ec2-3-136-157-90.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaPets = 'http://ec2-3-22-61-127.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
    cadenaHouseful = ''
    cadenaElectro = 'http://ec2-3-139-57-54.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'

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
            for i in range(23):
                valores.append('APAGADO')
        if type_of_cadena == 'grafica':
            for i in range(23):
                valores.append(0)
    return valores
