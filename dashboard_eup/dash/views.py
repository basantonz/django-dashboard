from django.shortcuts import render

tablita = ['dato1\t','dato2\t','dato3\t','dato4\t','dato5\t']

def home(request):
	context = {'tablita':tablita}
	return render (request , "dash/home.html", context) 