from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import Lugar
from usuarios.models import Usuario
from .forms import RegistroLugarForm
from django.urls import reverse_lazy

class LugaresView(ListView):
    model = Lugar
    template_name = 'lugares.html'
    paginate_by = 10


class RegistroLugarView(FormView):
    model = Lugar
    template_name = 'registroLugar.html'
    success_url = reverse_lazy('lugares')
    form_class = RegistroLugarForm

    def form_valid(self, form):
        print("Entra en form_valid de RegistroLugarView")
        lugar = form.save()
        lugar.name = form.cleaned_data['name'].title()
        if self.request.user:
            lugar.admin = Usuario.objects.get(username = self.request.user.username)
        lugar.save()
        return super(RegistroLugarView, self).form_valid(form)