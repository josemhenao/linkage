from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView, DeleteView, UpdateView, View
from django.shortcuts import render
from .forms import LoginForm, RegisterForm, ChangePasswordForm, ChangeImageForm
from .models import Usuario
from . import global_vars

class UsuariosView(TemplateView):
    template_name = 'usuarios.html'

class RegisterView(FormView):
    model = Usuario
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')  # La redirección está funcionando

    def form_valid(self, form):
        user = form.save()
        user.set_password(form.cleaned_data['password'])
        user.confirm_password = ''
        user.save()
        return super(RegisterView, self).form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print("--> Form valid del LoginView")
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('home'))

class ChangePasswordView(FormView):
    template_name = 'change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        print("Entra en el form_valid() de ChangePasswordView...")
        user = Usuario.objects.get(username = form.cleaned_data['username'])
        print("Cambiando Password...")
        user.set_password(form.cleaned_data['new_password'])
        print("Guardando los cambios realizados...")
        user.save()
        print("Retornando")
        return super(ChangePasswordView, self).form_valid(form)

class ChangeImageView(FormView):
    template_name = 'change_profile_image.html'
    form_class = ChangeImageForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        print("--> Entra en el form_valid() de ChangeImageView...")
        user = Usuario.objects.get(username = self.kwargs['username'])
        user.imagen = form.cleaned_data['imagen']

        if form.cleaned_data['imagen'] != global_vars.DEFAULT_USER_IMAGE:
            user.save()
            print("--> Se ha modificado la imagen")
        else:
            print("--> No se ha modificado la imagen")
        return super(ChangeImageView, self).form_valid(form)

def ProfileView(request, username=None):
    if username:
        user = Usuario.objects.get(username=username)
    else:
        user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)

class ProfileViewClass (UpdateView):
    model = Usuario
    context_object_name = 'user'

def DeleteView(request, username=None):
    if username:
        user = Usuario.objects.get(username=username)
    else:
        user = request.user
    context = {'usuario': user}
    return render(request, 'delete_usuario.html', context)

