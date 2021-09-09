from django.shortcuts import render

tablita = ['datatable1','datatable2','datatable3']

def home(request):
	context = {'tablita':tablita}
	return render (request , "dash/home.html", context) 