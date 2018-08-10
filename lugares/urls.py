from django.urls import path

from .views import LugaresView, RegistroLugarView, DetalleLugarView, ChangeImageView

urlpatterns = [
    path('', LugaresView.as_view(), name='lugares'),
    path('register', RegistroLugarView.as_view(), name='lugares_register'),
    path('<slug:slug>/detalle', DetalleLugarView.as_view(), name='lugares_detail'),
    path('<slug:slug>/cambiar_imagen', ChangeImageView.as_view(), name='lugares_change_image'),
]
