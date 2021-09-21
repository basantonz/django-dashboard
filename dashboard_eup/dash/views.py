from django.shortcuts import render
import requests
import json
from .controllers.dashControllers import ConvertirLista

cadenaFashion = 'http://ec2-18-222-217-205.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
cadenaKid = 'http://ec2-3-136-157-90.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
cadenaPets = 'http://ec2-3-22-61-127.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
cadenaHouseful = ''
cadenaElectro = 'http://ec2-3-139-57-54.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'


def home(request):
    listaFashion = ConvertirLista(cadenaFashion, "web")
    print('lista fashion ok')
    listaKid = ConvertirLista(cadenaKid, "web")
    listaPets = ConvertirLista(cadenaPets, "web")
    listaHouseful = ConvertirLista(cadenaHouseful, "web")
    listaElectro = ConvertirLista(cadenaElectro, "web")

    tablita = ['datatable1', 'datatable2', 'datatable3']
    tablita2 = ['datatable4', 'datatable5']
    context = {'tablita': tablita,
               'tablita2': tablita2,

               'listaFashion': listaFashion,
               'listaKid': listaKid,
               'listaPets': listaPets,
               'listaHouseful': listaHouseful,
               'listaElectro': listaElectro
               }
    return render(request, "dash/home.html", context)

def graficos(request):
    return render(request, "dash/graficos.html")