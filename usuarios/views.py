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


class AuthView(TemplateView):
    template_name = 'auth.html'


class DeleteUsuarioView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('auth.html')


class UpdateUsuarioView(UpdateView):
    model = Usuario
    fields = ['username', 'first_name', 'last_name', 'tipo_id', 'identificacion']
    template_name = 'update_usuario.html'

class ChangePasswordView(FormView):
    template_name = 'register.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = Usuario.objects.get(username = form.cleaned_data['username'])
        user.set_password(form.cleaned_data['new_password'])
        user.save()
        return super(RegisterView, self).form_valid(form)

# class DetalleUsuarioView(DetailView):
#     model = Usuario
#     template_name = 'profile.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['username'] = Usuario.objects.get(username__in=self.)
#         return context

def ProfileView(request, username=None):
    if username:
        user = Usuario.objects.get(username=username)
    else:
        user = request.user
    args = {'usuario': user}
    return render(request, 'profile.html', args)
