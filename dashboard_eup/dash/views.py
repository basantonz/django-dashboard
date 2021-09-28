from django.shortcuts import render
import requests
import json
from .controllers.dashControllers import ConvertirLista, ConvertirLista2
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
    ultimos_sub_Fashion = Fashion.objects.all().order_by('-idFashion')[:1]
    ultimos_sub_Kid = Kid.objects.all().order_by('-idKid')[:1]
    ultimos_sub_Pets = Pets.objects.all().order_by('-idPets')[:1]
    ultimos_sub_Houseful = Houseful.objects.all().order_by('-idHouseful')[:1]
    ultimos_sub_Electro = Electro.objects.all().order_by('-idElectro')[:1]

    listaFashion = ConvertirLista2("fashion", 1)
    listaKid = ConvertirLista2("kid", 1)
    listaPets = ConvertirLista2("pets", 1)
    listaHouseful = ConvertirLista2("houseful", 1)
    listaElectro = ConvertirLista2("electro", 1)
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

def tiendas(request):
    FashionAllArr=ConvertirLista2("fashion",6)
    KidAllArr=ConvertirLista2("kid",6)
    PetsAllArr=ConvertirLista2("pets",6)
    HousefulAllArr=ConvertirLista2("houseful",6)
    ElectroAllArr=ConvertirLista2("electro",6)
    
    context = {'FashionAllArr': FashionAllArr,
                'KidAllArr': KidAllArr,
                'PetsAllArr': PetsAllArr,
                'HousefulAllArr': HousefulAllArr,
                'ElectroAllArr': ElectroAllArr 
               }
    return render(request, "dash/tiendas.html",context)

def fashion(request):
    FashionAllArr=ConvertirLista2("fashion",6)
    context = {'FashionAllArr': FashionAllArr,}
    return render(request, "dash/tiendas/fashion.html",context)

def kid(request):
    KidAllArr=ConvertirLista2("kid",6)
    context = {'KidAllArr': KidAllArr,}
    return render(request, "dash/tiendas/kid.html",context)

def pets(request):
    PetsAllArr=ConvertirLista2("pets",6)
    context = {'PetsAllArr': PetsAllArr,}
    return render(request, "dash/tiendas/pets.html",context)

def houseful(request):
    HousefulAllArr=ConvertirLista2("houseful",6)
    context = {'HousefulAllArr': HousefulAllArr,}
    return render(request, "dash/tiendas/houseful.html",context)

def electro(request):
    ElectroAllArr=ConvertirLista2("electro",6)
    context = {'ElectroAllArr': ElectroAllArr,}
    return render(request, "dash/tiendas/electro.html",context)

def configuracion(request):
    a='a'
    context = {'a': a,}
    return render(request, "dash/configuracion.html",context)

def usuarios(request):
    a='a'
    context = {'a': a,}
    return render(request, "dash/usuarios.html",context)