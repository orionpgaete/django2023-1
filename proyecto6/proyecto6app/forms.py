from django import forms
from django.core import validators
from proyecto6app.models import Proyecto


class FormProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'


        nombre = forms.CharField()
        fechaInicio = forms.DateField()
