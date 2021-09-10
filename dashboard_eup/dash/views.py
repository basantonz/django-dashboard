from django.shortcuts import render

tablita = ['datatable1','datatable2','datatable3']
tablita2 = ['datatable4','datatable5']

def home(request):
	context = { 'tablita':tablita,
				'tablita2':tablita2
	}
	return render (request , "dash/home.html", context) 