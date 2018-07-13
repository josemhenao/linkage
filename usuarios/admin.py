from django.contrib import admin

from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'tipo_id', 'identificacion')
    list_filter = ('username', 'identificacion', 'birth_date', 'last_login')
    ordering = ['username']


admin.site.register(Usuario, UsuarioAdmin)
