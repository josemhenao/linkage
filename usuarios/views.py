from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, CreateView, TemplateView, DeleteView, UpdateView, View, DetailView
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from passlib.hash import sha256_crypt
from .forms import RegisterForm

from .models import Usuario

class RegisterView(FormView):
    model = Usuario
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')  # La redirección está funcionando

    def form_valid(self, form):
        self.crear_usuario(form)
        return super(RegisterView, self).form_valid(form)

    def crear_usuario(self, form):
        raw_password = form.cleaned_data['password']
        user = Usuario.objects.create_user(
            username = form.cleaned_data['username'],
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            email = form.cleaned_data['email'],
            birth_date = form.cleaned_data['birth_date'],
            imagen = form.cleaned_data['imagen'],
            tipo_id = form.cleaned_data['tipo_id'],
            identificacion = form.cleaned_data['identificacion'],
        )

        user.set_password(raw_password)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print("form_valid() de LoginView")
        raw_password = form.cleaned_data['password']
        print (raw_password)
        print(sha256_crypt.hash(raw_password))
        user = authenticate(
            username = form.cleaned_data['username'],
            password = sha256_crypt.hash(raw_password)
        )
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('home'))

class AuthView(TemplateView):
    template_name = 'auth.html'

class DeleteUsuarioView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('auth.html')

class UpdateUsuarioView(UpdateView):
    model = Usuario
    fields = ['username','nombre','apellido','tipo_id','identificacion','imagen']
    template_name = 'update_usuario.html'

class DetalleUsuarioView(DetailView):
    model = Usuario