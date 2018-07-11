from builtins import print

from django import forms
from  .models import Usuario

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password','confirm_password', 'birth_date','imagen','tipo_id','identificacion']

        widgets = {
            'username': forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'Username',
                'required': True,
                'unique':True,
                'size': 25
            }),
            'first_name': forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'Nombre',
                'required': True,
                'size': 25,
            }),
            'last_name': forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'Apellido',
                'size': 25
            }),
            'email': forms.TextInput(attrs={
                'type': 'email',
                'placeholder': 'Email',
                'required': True,
                'size': 30
            }),
            'password': forms.TextInput(attrs={
                'type': 'password',
                'placeholder': 'Contraseña',
                'required': True,
                'size': 25
            }),
            'confirm_password': forms.TextInput(attrs={
                'label':'confirama la contraseña',
                'type': 'password',
                'placeholder': 'Confirma la Contraseña',
                'required': True,
                'size': 25
            }),
            'birth_date': forms.DateInput(attrs={
                'format' : '%d/%m/%Y',
                'type':'date',
                'placeholder':'Formato dd/mm/yyyy',
                'size': 30

            }),
            'identificacion':forms.TextInput(attrs={
                'type':'text',
                'required': True,
                'size': 30
            })
        }

    def clean(self):
        print("entra en el clean del RegisterForm")

        # Validar si el username existe en la DB
        if self.user_exists():
            self.add_error('username','Nombre de usuario en uso')

        #Validar si el email se encuentra en la DB
        if self.email_exists():
            self.add_error('email', 'El email ingresado se encuentra en uso')

        # Validar si la contraseña coincide con la confirmación de la contraseña
        if not self.verify_psw():
            self.add_error('confirm_password', 'Las contraseñas no coinciden')

        # Validar si la Identificaición se encuentra en la DB
        if self.identificacion_exists():
            self.add_error('identificacion', 'La Identificación ingresada se encuentra registrada')


    def user_exists(self):
        print("Entra en user_exists()")
        user = Usuario.objects.filter(username=self.cleaned_data['username'])
        if user.exists():
            return True
        else:
            return False

    def email_exists(self):
        print("Verificando si el username existe...")
        email = Usuario.objects.filter(email = self.cleaned_data['email'])
        if email.exists():
            return True
        else:
            return False

    def verify_psw(self):
        print("Verificando las contraseñas...")
        psw = self.cleaned_data['password']
        conf_psw = self.cleaned_data['confirm_password']
        if psw == conf_psw:
            return True
        else:
            return False

    def identificacion_exists(self):
        print("Verificando si la identificación ya ha sido registrada...")
        """
        Verifica si la Identificación ingresada se encuantra segistrada en la base de datos, retorna False
        si no encuentra el valor y retorna True si encuentra un valor igual y ademas que se trate del mismo
        tipo de identificación
        """
        identificacion = Usuario.objects.filter(identificacion = self.cleaned_data['identificacion'], tipo_id = self.cleaned_data['tipo_id'])
        if identificacion.exists():
            return True
        else:
            return False

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
        if not user_found:
            self.add_error('username', 'Usuario no encontrado')
        else:
            user = Usuario.objects.get(username=self.cleaned_data['username'])
            if not user.check_password(self.cleaned_data['password']):
                self.add_error('password', 'La contraseña no coincide')


class ChangePasswordForm(forms.Form):

    username = forms.CharField(max_length=60, widget=forms.TextInput(attrs={
        'type':'text',
        'placeholder':'Username'
    }))

    old_password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'password',
        'placeholder': 'Contraseña Anterior'
    }))

    new_password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'password',
        'placeholder': 'Nueva Contraseña'
    }))

    conf_password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'password',
        'placeholder': 'Confirma la nueva contraseña'
    }))

    def clean(self):
        print("Entra en el clean() del ChangePasswordForm")
        user_exists = Usuario.objects.filter(username = self.cleaned_data['username']).exists()
        print("exists(): ", user_exists)
        if not user_exists:
            self.add_error('username', 'El username no existe')
        else: #Existe usuario
            user = Usuario.objects.get(username=self.cleaned_data['username'])
            if not self.check_password(user):
                self.add_error('old_password', 'La contraseña es incorrecta')
            if not self.verify_psws():
                self.add_error('conf_password','La confirmación no coincide')

    def check_password(self, user):
        print("Verificando la contraseña antigua")
        return user.check_password(self.cleaned_data['old_password'])

    def verify_psws(self):
        print("Verificando las contraseñas...")
        psw = self.cleaned_data['new_password']
        conf_psw = self.cleaned_data['conf_password']
        if psw == conf_psw:
            return True
        else:
            return False

class ChangeImageForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['imagen']