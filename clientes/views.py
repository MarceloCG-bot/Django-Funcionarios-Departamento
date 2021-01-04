from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def clientes(request):
    return HttpResponse('Maria, José, João')

def cliente_detalhe(request, id):
    return HttpResponse(id)

def cliente_por_nome(request, nome):
    return HttpResponse('ola %s' % nome)