from django.db.models import F
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import MeseroForm
from .models import Meseros
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializer import MeseroSerializer
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


def meseros_update_year(request):
    Meseros.objects.update(edad=F('edad')+5)
    meseros = Meseros.objects.all()
    return render(request, 'meseros/meseros3.html', context={
        'meseros': meseros
    })


# IMPLEMENTACION CON VISTAS BASADAS EN CLASES

class MeseroListPeru(ListView):
    model = Meseros
    template_name = 'meseros/meseros_peru.html'


class MeseroList(ListView):
    model = Meseros
    template_name = 'meseros/meseros.html'


class MeseroCreate(CreateView):
    model = Meseros
    form_class = MeseroForm
    template_name = 'meseros/mesero_create.html'
    success_url = reverse_lazy('meseros_list_vbc')


class MeseroUpdate(UpdateView):
    model = Meseros
    form_class = MeseroForm
    template_name = 'meseros/mesero_update.html'
    success_url = reverse_lazy('meseros_list_vbc')


class MeseroDelete(DeleteView):
    model = Meseros
    success_url = reverse_lazy('meseros_list')
    template_name = 'meseros/mesero_delete.html'

# API


@api_view(['GET', 'PUT', 'DELETE'])
def mesero_update_api(request, pk):
    mesero = Meseros.objects.filter(id=pk).first()
    if mesero:
        if request.method == 'GET':
            serializers_class = MeseroSerializer(mesero)
            return Response(serializers_class.data)
        elif request.method == 'PUT':
            serializers_class = MeseroSerializer(mesero, data=request.data)
            if serializers_class.is_valid():
                serializers_class.save()
                return Response(serializers_class.data, status=status.HTTP_200_OK)
            return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            mesero.delete()
            return Response('Mesero ha sido eliminado correctamente de la BD', status=status.HTTP_200_OK)