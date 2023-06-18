from django.urls import path
from apps.meseros import views

urlpatterns = [
    path('meseros_list/', views.meseros_list, name='meseros_list'),
    path('meseros_list_filter/', views.meseros_list_filter, name='meseros_list_filter'),
    path('meseros_list_2/', views.meseros_update_year, name='meseros_list_2'),
    path('meseros_peru/', views.MeseroListPeru.as_view(), name='meseros_peru'),
    path('meseros_list_vbc/', views.MeseroList.as_view(), name='meseros_list_vbc'),
    path('meseros_create_vbc/', views.MeseroCreate.as_view(), name='meseros_create_vbc'),
    path('meseros_update_vbc/<int:pk>', views.MeseroUpdate.as_view(), name='meseros_update_vbc'),
    path('meseros_delete_vbc/<int:pk>', views.MeseroDelete.as_view(), name='meseros_delete_vbc'),
    path('meseros_update_api/<int:pk>', views.mesero_update_api, name='meseros_update_api')
]
