from django.shortcuts import render
import requests
import json
from .controllers.dashControllers import ConvertirLista
from dash.models import Fashion, Kid, Pets, Houseful, Electro

#cadenaFashion = 'http://ec2-18-222-217-205.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
#cadenaKid = 'http://ec2-3-136-157-90.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
#cadenaPets = 'http://ec2-3-22-61-127.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
#cadenaHouseful = ''
#cadenaElectro = 'http://ec2-3-139-57-54.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'

cadenaFashion = ''
cadenaKid = ''
cadenaPets = ''
cadenaHouseful = ''
cadenaElectro = ''

def home(request):
    listaFashion = ConvertirLista(cadenaFashion, "web")
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
    listaFashion = ConvertirLista(cadenaFashion, "grafica")
    listaKid = ConvertirLista(cadenaKid, "grafica")
    listaPets = ConvertirLista(cadenaPets, "grafica")
    listaHouseful = ConvertirLista(cadenaHouseful, "grafica")
    listaElectro = ConvertirLista(cadenaElectro, "grafica")

    ultimos_sub_Fashion = Fashion.objects.all().order_by('idFashion')[1:].distinct('all_products')
    ultimos_sub_Kid = Kid.objects.all().order_by('idKid')[1:].distinct('all_products')
    ultimos_sub_Pets = Pets.objects.all().order_by('idPets')[1:].distinct('all_products')
    ultimos_sub_Houseful = Houseful.objects.all().order_by('idHouseful')[1:].distinct('all_products')
    ultimos_sub_Electro = Electro.objects.all().order_by('idElectro')[1:].distinct('all_products')
    print(ultimos_sub_Fashion)

    context = {'listaFashion': listaFashion,
               'listaKid': listaKid,
               'listaPets': listaPets,
               'listaHouseful': listaHouseful,
               'listaElectro': listaElectro,
               'ultimos_sub_Fashion': ultimos_sub_Fashion,
               'ultimos_sub_Kid': ultimos_sub_Kid,
               'ultimos_sub_Pets': ultimos_sub_Pets,
               'ultimos_sub_Houseful': ultimos_sub_Houseful,
               'ultimos_sub_Electro': ultimos_sub_Electro  
               }
    return render(request, "dash/graficos.html",context)