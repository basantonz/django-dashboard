from django.shortcuts import render
import requests
import json
from .controllers.dashControllers import ConvertirLista, ConvertirLista2
from dash.models import Fashion, Kids, BeautyHealth, HouseHome, Electro

#cadenaFashion = 'http:/ec2-18-218-217-186.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
#cadenaKids = 'http://ec2-18-117-168-228.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
#cadenaBeautyHealth = 'http://ec2-18-218-117-226.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
#cadenaHouseHome = 'http://	ec2-18-117-219-250.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
#cadenaElectro = 'http://ec2-18-118-170-239.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'

cadenaFashion = 'http:/ec2-18-218-217-186.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
cadenaKids = 'http://ec2-18-117-168-228.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
cadenaBeautyHealth = 'http://ec2-18-218-117-226.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
cadenaHouseHome = 'http://	ec2-18-117-219-250.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
cadenaElectro = 'http://ec2-18-118-170-239.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'

def home(request):
    ultimos_sub_Fashion = Fashion.objects.all().order_by('-idFashion')[:1]
    ultimos_sub_Kids = Kids.objects.all().order_by('-idKids')[:1]
    ultimos_sub_BeautyHealth = BeautyHealth.objects.all().order_by('-idBeautyHealth')[:1]
    ultimos_sub_HouseHome = HouseHome.objects.all().order_by('-idHouseHome')[:1]
    ultimos_sub_Electro = Electro.objects.all().order_by('-idElectro')[:1]

    listaFashion = ConvertirLista2("fashion", 1)
    listaKids = ConvertirLista2("kids", 1)
    listaBeautyHealth = ConvertirLista2("beautyhealth", 1)
    listaHouseHome = ConvertirLista2("househome", 1)
    listaElectro = ConvertirLista2("electro", 1)
    tablita = ['datatable1', 'datatable2', 'datatable3']
    tablita2 = ['datatable4', 'datatable5']
    context = {'tablita': tablita,
               'tablita2': tablita2,
               
               'listaFashion': listaFashion,
               'listaKids': listaKids,
               'listaBeautyHealth': listaBeautyHealth,
               'listaHouseHome' : listaHouseHome,
               'listaElectro' : listaElectro,
               }
    return render(request, "dash/home.html", context)

def tiendas(request):
    FashionAllArr=ConvertirLista2("fashion",6)
    KidsAllArr=ConvertirLista2("kids",6)
    BeautyHealthAllArr=ConvertirLista2("beautyhealth",6)
    HouseHomeAllArr=ConvertirLista2("househome",6)
    ElectroAllArr=ConvertirLista2("electro",6)
    
    context = {'FashionAllArr': FashionAllArr,
                'KidsAllArr': KidsAllArr,
                'BeautyHealthAllArr': BeautyHealthAllArr,
                'HouseHomeAllArr': HouseHomeAllArr,
                'ElectroAllArr': ElectroAllArr,
                }
    return render(request, "dash/tiendas.html",context)

def fashion(request):
    FashionAllArr=ConvertirLista2("fashion",6)
    context = {'FashionAllArr': FashionAllArr,}
    return render(request, "dash/tiendas/fashion.html",context)

def kids(request):
    KidsAllArr=ConvertirLista2("kids",6)
    context = {'KidsAllArr': KidsAllArr,}
    return render(request, "dash/tiendas/kids.html",context)

def beautyhealth(request):
    BeautyHealthAllArr=ConvertirLista2("beautyhealth",6)
    context = {'BeautyHealthAllArr': BeautyHealthAllArr,}
    return render(request, "dash/tiendas/beautyhealth.html",context)

def househome(request):
    HouseHomeAllArr=ConvertirLista2("househome",6)
    context = {'HouseHomeAllArr': HouseHomeAllArr,}
    return render(request, "dash/tiendas/househome.html",context)

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