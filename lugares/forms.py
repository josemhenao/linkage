from django import forms
from .models import Lugar

class RegistroLugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['name', 'description', 'capacity', 'addres', 'city', 'img_ppal', 'img_slide']

    def clean(self):
        print("Entra en clean() de form")
        print(self.cleaned_data)
        name_enc =  Lugar.objects.filter(name = self.cleaned_data['name'].capitalize())
        if not self.validate_capacity():
            self.add_error('capacity','Ingresa una cantidad válida')

    def validate_capacity(self):
        print("Entra en validate_capacity()")
        capacity_in = self.cleaned_data['capacity']
        if capacity_in < 1:
            return False
        else:
            return True

