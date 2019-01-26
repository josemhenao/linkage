from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, FormView, DetailView, UpdateView
from .models import Lugar
from usuarios.models import Usuario
from .forms import RegistroLugarForm, ChangeImageForm
from django.urls import reverse_lazy
from . import global_vars

class LugaresView(ListView):
    model = Lugar
    template_name = 'lugares.html'
    paginate_by = 20


class RegistroLugarView(LoginRequiredMixin, FormView):
    model = Lugar
    template_name = 'registroLugar.html'
    success_url = reverse_lazy('lugares')
    form_class = RegistroLugarForm

    def form_valid(self, form):
        print("Entra en form_valid de RegistroLugarView")
        lugar = form.save()
        lugar.nombre = form.cleaned_data['nombre'].title()
        if self.request.user:
            lugar.admin = Usuario.objects.get(username = self.request.user.username)
        else:
            lugar.admin = Usuario.objects.get(id=1)
        lugar.save()
        return super(RegistroLugarView, self).form_valid(form)


class DetalleLugarView(DetailView):
    model = Lugar
    template_name = 'detalle_lugar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# class ChangeImageView(FormView):
#     template_name = 'change_profile_image.html'
#     form_class = ChangeImageForm
#     success_url = reverse_lazy('lugares')
#
#     def form_valid(self, form):
#         print("--> Entra en el form_valid() de ChangeImageView...")
#         lugar = Lugar.objects.get(slug=self.kwargs['slug'])
#         lugar.img_ppal = form.cleaned_data['img_ppal']
#
#         if form.cleaned_data['img_ppal'] != global_vars.DEFAULT_USER_IMAGE:
#             lugar.save()
#             print("--> Se ha modificado la imagen")
#         else:
#             print("--> No se ha modificado la imagen")
#         return super(ChangeImageView, self).form_valid(form)

class UpdateLugarView(LoginRequiredMixin, UpdateView):
    model = Lugar
    fields = ['nombre','descripcion', 'img_ppal','ciudad','direccion', 'capacidad']
    template_name = 'lugares_update_lugar.html'
    success_url = reverse_lazy('lugares')