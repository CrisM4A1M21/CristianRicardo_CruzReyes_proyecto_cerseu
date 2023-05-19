from django.contrib import admin
from platos.models import Platos
# Register your models here.


@admin.register(Platos)
class PlatosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio")
    search_fields = ("nombre",)


