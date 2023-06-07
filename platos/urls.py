from django.urls import path
from platos import views

urlpatterns = [
    path('platos_list/', views.platos_list, name='platos_list'),
    path('platos_list2/', views.platos_list2, name='platos_list2'),
]