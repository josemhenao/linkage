from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate

from .models import Usuario

class RegisterView(FormView):

    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login') # La redirección está funcionando

    tipos_id = ['Cédula de Ciudadanía','Targeta de Identidad','Pasaporte','Cédula de Extrangería']

    #def form_valid(self, form):
    #    print(form.cleaned_data['username'])
    #    print(form.cleaned_data['nombre'])



class LoginView(FormView):

    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )

        login(self.request, user)
        return super(LoginView, self).form_valid(form)