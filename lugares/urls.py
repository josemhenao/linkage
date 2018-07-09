from django.urls import path

from .views import LugaresView, RegistroLugarView

urlpatterns = [
    path('', LugaresView.as_view(), name='lugares'),
    path('register', RegistroLugarView.as_view(),name='registrar_lugar'),
]