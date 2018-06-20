from django.shortcuts import render
from django.views.generic import TemplateView

class RegisterView(TemplateView):
    template_name = 'register.html'

class LoginView(TemplateView):
    template_name = 'login.html'
