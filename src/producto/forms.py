from django import forms
from . import models

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ["nombre"]
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre","")
        if len(nombre)<3:
            raise forms.ValidationError("La longitud debe ser mayor a 3 caracteres")
        if not nombre.isalpha():
            raise forms.ValidationError("La categoría no puede contener numeros")
        return nombre