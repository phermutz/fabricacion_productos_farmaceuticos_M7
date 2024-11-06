from django.contrib import admin
from .models import Producto, Laboratorio, DirectorGeneral

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'laboratorio', 'anio_fabricacion', 'precio_costo', 'precio_venta')
    list_filter = ('laboratorio',)

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'pais')

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'laboratorio')
