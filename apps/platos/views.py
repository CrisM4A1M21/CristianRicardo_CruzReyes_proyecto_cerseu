from django.db.models import Q
from django.shortcuts import render
from .models import Platos
from django.core import serializers as ssr
from django.http import HttpResponse

# Create your views here.


def platos_list(request):
    platos = Platos.objects.all()
    return render(request, 'platos/platos.html', context={
        'platos': platos
    })


def platos_list2(request):
    plato1 = Platos(nombre="Salchipapa", precio=42, procedencia="Peru")
    plato1.save()
    plato2 = Platos(nombre="Arroz con pollo", precio=50, procedencia="Peru")
    plato2.save()
    plato3 = Platos(nombre="Seco a la norteña", precio=60, procedencia="Peru")
    plato3.save()

    platos = Platos.objects.filter(procedencia="Peru", precio__gt=40)

    return render(request, 'platos/platos2.html', context={
        'platos': platos
    })

# SERIALIZERS


def ListPlatosSerializer(request):
    query = Q(precio__gte=50)
    list_platos = ssr.serialize('json', Platos.objects.filter(query), fields=['nombre', 'precio', 'procedencia'])
    return HttpResponse(list_platos, content_type='application/json')
