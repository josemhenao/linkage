from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView, DeleteView, UpdateView, View
from django.shortcuts import render
from .forms import LoginForm, RegisterForm, ChangePasswordForm
from .models import Usuario


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
        print("Form valid del LoginView")
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


class UsuariosView(TemplateView):
    template_name = 'usuarios.html'

class UpdateUsuarioView(UpdateView):
    model = Usuario
    fields = ['username', 'first_name', 'last_name', 'tipo_id', 'identificacion']
    template_name = 'update_usuario.html'
    context_object_name = 'user'

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

def ProfileView(request, username=None):
    if username:
        user = Usuario.objects.get(username=username)
    else:
        user = request.user
    context = {'usuario': user}
    return render(request, 'profile.html', context)


def DeleteView(request, username=None):
    if username:
        user = Usuario.objects.get(username=username)
    else:
        user = request.user
    context = {'usuario': user}
    return render(request, 'delete_usuario.html', context)

