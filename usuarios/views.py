from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from passlib.hash import pbkdf2_sha256

from .models import Usuario

class RegisterView(CreateView):
    model = Usuario
    fields = ['username','first_name','last_name','email','password','tipo_id','identificacion','imagen','birth_date']
    template_name = 'register.html'
    success_url = reverse_lazy('login')  # La redirección está funcionando

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )

        login(self.request, user)
        return super(LoginView, self).form_valid(form)