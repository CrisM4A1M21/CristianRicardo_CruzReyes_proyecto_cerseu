from django.shortcuts import render
from .models import Meseros
# Create your views here.


def meseros_list(request):
    meseros = Meseros.objects.all()
    return render(request, 'meseros/meseros.html', context={
        'meseros': meseros
    })

def meseros_list_filter(request):
    meseros2 = Meseros.objects.filter(procedencia="Peru", edad__lt=30)
    return render(request, 'meseros/meseros2.html', context={
        'meseros2': meseros2
    })
