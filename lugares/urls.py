from django.urls import path

from .views import LugaresView, RegistroLugarView, DetalleLugarView, UpdateLugarView

urlpatterns = [
    path('', LugaresView.as_view(), name='lugares'),
    path('register', RegistroLugarView.as_view(), name='lugares_register'),
    path('<slug:slug>/detalle', DetalleLugarView.as_view(), name='lugares_detail'),
    path('<slug:slug>/actualizar', UpdateLugarView.as_view(), name='lugares_update_lugar'),
]
