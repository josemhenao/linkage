from django import forms
from django.contrib.admin import widgets
from  .models import Usuario
from passlib.hash import sha256_crypt

from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name','email','password','birth_date', 'imagen','tipo_id','identificacion')
        widgets = {
            'username': forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'Username'
            }),
            'first_name': forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'Nombre'
            }),
            'last_name': forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'Apellido'
            }),
            'email': forms.TextInput(attrs={
                'type': 'email',
                'placeholder': 'Email'
            }),
            'password': forms.TextInput(attrs={
                'type': 'password',
                'placeholder': 'Contraseña'
            }),
            'fecha_nacimiento': forms.DateInput(
                format='%d/%m/%Y'
            ),
        }

        # def clean(self):
        #     user_found = Usuario.objects.filter(username=self.cleaned_data['username']).exists()
        #     if not user_found:
        #         self.add
        #         self.add_error('username', 'El username está disponible')
        #     else:
        #         self.add_error('usermane', 'Username en uso')



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
        user_found = Usuario.objects.filter(username=self.cleaned_data['username']).exists()
        print("user_found = ",user_found)
        if not user_found:
            self.add_error('username', 'User no encontrado')
        else:
            user = Usuario.objects.get(username=self.cleaned_data['username'])
            print("usuario_pasw enconrado: ", user.password)
            raw_password = self.cleaned_data['password']
            print("raw_passw", raw_password)
            if not user.check_password(raw_password):
                self.add_error('password', 'la contraseña no coincide')
            else:
                self.add_error('password','la contraseña coincide')

# class ConsultaForm(forms.Form):
#     username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
#         'type':'text',
#         'placeholder': 'Consulta un username'
#     }))
