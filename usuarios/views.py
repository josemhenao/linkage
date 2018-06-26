from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate

from .models import Usuario

class RegisterView(CreateView):
    model = Usuario
    fields = '__all__'
    template_name = 'register.html'
    success_url = reverse_lazy('login')  # La redirección está funcionando

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