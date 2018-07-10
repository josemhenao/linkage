from django.contrib import admin
from .models import Lugar, Categoria


class LugarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad', 'direccion', 'ciudad')
    list_filter = ('nombre', 'capacidad', 'ciudad', 'categoria')
    list_per_page = 20

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'id_categoria', 'descripcion')
    list_per_page = 20


admin.site.register(Lugar, LugarAdmin)
admin.site.register(Categoria, CategoriaAdmin)
