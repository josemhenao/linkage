from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('birth_date', 'last_login')
    ordering = ['username']

admin.site.register(Usuario, UsuarioAdmin)
