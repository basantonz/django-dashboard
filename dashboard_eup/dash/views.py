from django.shortcuts import render
import requests,json


cadenaFashion='http://ec2-18-222-217-205.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
cadenaKid='http://ec2-3-136-157-90.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
cadenaPets='http://ec2-3-22-61-127.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'
cadenaHouseful=''
cadenaElectro='http://ec2-3-139-57-54.us-east-2.compute.amazonaws.com/api/v2.0/getStoreMetrics/'



def ConvertirLista(cadena):
	valores=[]
	try:
		datoObtenido=requests.get(cadena)
		lista=datoObtenido.json()
		for llave in lista:
			valores.append(lista[llave])
			print(lista[llave])
	except Exception as e:
		print(e)
		for i in range(23):
			valores.append('APAGADO')
	return valores

def home(request):
	listaFashion=ConvertirLista(cadenaFashion)
	print('lista fashion ok')
	listaKid=ConvertirLista(cadenaKid)
	listaPets=ConvertirLista(cadenaPets)
	listaHouseful=ConvertirLista(cadenaHouseful)
	listaElectro=ConvertirLista(cadenaElectro)

	tablita = ['datatable1','datatable2','datatable3']
	tablita2 = ['datatable4','datatable5']
	context = { 'tablita':tablita,
				'tablita2':tablita2,

				'listaFashion': listaFashion,
				'listaKid':listaKid,
				'listaPets':listaPets,
				'listaHouseful':listaHouseful,
				'listaElectro':listaElectro
	}
	return render (request , "dash/home.html", context) 
