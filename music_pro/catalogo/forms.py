from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Contacto
        #fields = {"nombre", "correo", "tipo_consulta", "mensaje", "avisos"}
        fields = '__all__'