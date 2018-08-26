from django.shortcuts import render

def index(request):
	return render (request,'index.html')

def application(request):
	return render (request,'accounting/application.html')