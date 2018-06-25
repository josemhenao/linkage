from django.shortcuts import render
from django.views.generic import TemplateView

class EventosView(TemplateView):
    template_name = "eventos.html"

