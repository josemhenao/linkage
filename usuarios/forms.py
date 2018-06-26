from django import forms
from django.contrib.admin import widgets

from django.contrib.auth.models import User

#class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ('username', 'first_name', 'last_name','email','password','fecha_nacimiento', 'rol','tipo_id','identificacion')
#         widgets = {
#             'username': forms.TextInput(attrs={
#                 'type': 'text',
#                 'placeholder': 'Username'
#             }),
#             'first_name': forms.TextInput(attrs={
#                 'type': 'text',
#                 'placeholder': 'Nombre'
#             }),
#             'last_name': forms.TextInput(attrs={
#                 'type': 'text',
#                 'placeholder': 'Apellido'
#             }),
#             'email': forms.TextInput(attrs={
#                 'type': 'email',
#                 'placeholder': 'Email'
#             }),
#             'password': forms.TextInput(attrs={
#                 'type': 'password',
#                 'placeholder': 'Contraseña'
#             }),
#             'fecha_nacimiento': forms.DateInput(
#                 format='%d/%m/%Y'
#             ),
#         }
#
#         def clean(self):
#             user_found = Usuario.objects.filter(username=self.cleaned_data['username']).exists()
#             if not user_found:
#                 self.add_error('username', 'El username está disponible')
#             else:
#                 self.add_error('usermane', 'Username en uso')
#


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'text',
        'placeholder': 'Username'
    }))

    password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'password',
        'placeholder': 'Password'
    }))

    def clean(self):
        print("entrando en def clean de LoginForm")
        print(self.cleaned_data)
        user_found = User.objects.filter(username=self.cleaned_data['username']).exists()
        if not user_found:
            self.add_error('username', 'User no encontrado')
        else:
            user = User.objects.get(username=self.cleaned_data['username'])
            if not user.check_password(self.cleaned_data['password']):
                self.add_error('password', 'La contraseña no coincide')

# class ConsultaForm(forms.Form):
#     username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
#         'type':'text',
#         'placeholder': 'Consulta un username'
#     }))
