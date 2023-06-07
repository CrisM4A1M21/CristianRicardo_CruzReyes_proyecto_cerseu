from django.urls import path
from meseros import views

urlpatterns = [
    path('meseros_list/', views.meseros_list, name='meseros_list'),
    path('meseros_list_filter/', views.meseros_list_filter, name='meseros_list_filter')

]