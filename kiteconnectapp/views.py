from django.shortcuts import render

def index(request):
	return render(request, 'kiteconnectapp/index.html', context={'text': 'Hello World'})