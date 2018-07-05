from django import forms
from .models import Lugar

class RegistroLugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['name', 'description', 'capacity', 'addres', 'city', 'img_ppal', 'img_slide']

    def clean(self):
        print("Entra en clean() de form")
        print(self.cleaned_data)

        if not self.validate_capacity():
            self.add_error('capacity','Ingresa una cantidad válida')

        if self.validate_lugar():
            self.add_error('name','Ya existe un lugar registrado con el mismo nombre en la misma ciudad')

    def validate_capacity(self):
        print("Entra en validate_capacity()")
        capacity_in = self.cleaned_data['capacity']
        if capacity_in < 1:
            return False
        else:
            return True

    def validate_lugar(self):
        print("Entra en validate_lugar()")
        lugar_enc = Lugar.objects.filter(name=self.cleaned_data['name'], city=self.cleaned_data['city'])
        print("lugar: ", lugar_enc)
        if lugar_enc.exists():
            return True
        else:
            return False

