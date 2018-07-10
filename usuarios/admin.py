from django.contrib import admin
from .models import Usuario, Rol, Permiso

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','tipo_id','identificacion')
    list_filter = ('username','identificacion','birth_date','last_login')


class PermisoAdmin (admin.ModelAdmin):
    list_display = ('id_permiso','permiso','descripcion')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Rol)
admin.site.register(Permiso, PermisoAdmin)