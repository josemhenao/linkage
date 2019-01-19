from django import forms
from .models import Lugar, Categoria

class RegistroLugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['nombre', 'descripcion', 'capacidad', 'direccion', 'ciudad','categoria', 'img_ppal','imagenes', 'admin']

        widgets ={
            'categoria': forms.CheckboxSelectMultiple()
        }
    def clean(self):
        print("Entra en clean() de form")
        print(self.cleaned_data)

        # if not self.request.user:
        #     self.add_error('admin','Debes estár logueado en la plataforma')

        if not self.validate_capacity():
            self.add_error('capacidad','Ingresa una cantidad válida')

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