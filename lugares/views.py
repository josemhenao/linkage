from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import Lugar
from .forms import RegistroLugarForm
from django.urls import reverse_lazy

class LugaresView(ListView):
    model = Lugar
    template_name = 'lugares.html'

class RegistroLugarView(FormView):
    model = Lugar
    template_name = 'registroLugar.html'
    success_url = reverse_lazy('home')
    form_class = RegistroLugarForm

    def form_valid(self, form):
        print("entra en form_valid de RegistroLugarView")
        lugar = form.save()
        lugar.name = form.cleaned_data['name'].capitalize()
        lugar.save()
        return super(RegistroLugarView, self).form_valid(form)