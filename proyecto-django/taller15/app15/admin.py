from django.contrib import admin

from .models import *

class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula')
    search_fields = ('nombre', 'apellido')

admin.site.register(Propietario, PropietarioAdmin)

class EdificioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'tipo')

admin.site.register(Edificio, EdificioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'costo', 'num_cuartos', 'edificio')
    search_fields = ('propietario', 'costo')

admin.site.register(Departamento, DepartamentoAdmin)