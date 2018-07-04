from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Lugar
from django.urls import reverse_lazy

class LugaresView(ListView):
    model = Lugar
    template_name = 'lugares.html'

class RegistroLugarView(CreateView):
    model = Lugar
    template_name = 'registroLugar.html'
    fields = ['id_lugar','name','description','capacity','addres','city','img_ppal','img_slide']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        lugar = form.save()
        lugar.save()
        return super(RegistroLugarView, self).form_valid(form)



