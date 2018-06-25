from django.urls import path

from .views import EventosView

urlpatterns = [
    path('', EventosView.as_view(), name='eventos'),
]