from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def bienvenido(request):
    #return HttpResponse('Hole mundo desde Django')
    return render(request, 'index.html')