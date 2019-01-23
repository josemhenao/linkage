from django import forms
from django.template.defaultfilters import slugify

from .models import Lugar, Categoria

class RegistroLugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['nombre', 'descripcion', 'capacidad', 'direccion', 'ciudad', 'img_ppal','imagenes']

        widgets ={
            'categoria': forms.CheckboxSelectMultiple()
        }

    def clean(self):
        print("Entra en clean() de RegistroLugarForm")
        print(self.cleaned_data)

        # Verificar que la capacida ingresada no sea un número extraño
        if not self.validate_capacity():
            self.add_error('capacidad','Ingresa una cantidad válida')

        # Verificar que no exista un Lugar similar registrado
        if self.validate_lugar():
            self.add_error('nombre','Ya existe un lugar registrado con el mismo nombre en la misma ciudad')


    def validate_capacity(self):
        print("Entra en validate_capacity()")
        capacidad_in = self.cleaned_data['capacidad']
        if capacidad_in < 1:
            return False
        else:
            return True

    def validate_lugar(self):
        print("Entra en validate_lugar()")
        lugar_enc = Lugar.objects.filter(nombre=self.cleaned_data['nombre'], ciudad=self.cleaned_data['ciudad'])
        print("lugar: ", lugar_enc)
        if lugar_enc.exists():
            return True
        else:
            return False

class ChangeImageForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['img_ppal']

    def clean(self):
        print('--> Entra en el clean() de ChangeImageForm')
        print('image: ', self.cleaned_data['img_ppal'])
        if self.cleaned_data['img_ppal'] == '':
            self.add_error('img_ppal','Selecciona una imagen')