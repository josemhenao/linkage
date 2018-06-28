from django.contrib import admin
from .models import Usuario, Rol, Permiso

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email')
    list_filter = ('username','identificacion','birth_date','last_login')


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Rol)
admin.site.register(Permiso)