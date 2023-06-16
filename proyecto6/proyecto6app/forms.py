from django import forms
from django.core import validators
from proyecto6app.models import Proyecto


class FormProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class IngresoForm(forms.Form):
        
        fechaInicio = forms.DateField()
        fechaInicio.widget.attrs['class'] = 'form-control'
        
        fechaTermino = forms.DateField()
        fechaTermino.widget.attrs['class'] = 'form-control' 

        nombre = forms.CharField(max_length=50)
        nombre.widget.attrs['class'] = 'form-control'

        responsable = forms.CharField(max_length=50)
        responsable.widget.attrs['class'] = 'form-control'

        prioridad = forms.IntegerField(validators=(validators.MinValueValidator(1), validators.MaxValueValidator(15)))  
        prioridad.widget.attrs['class'] = 'form-control'       

        

def clean_nombre(self):
    inputNombre = self.clean_data['nombre']
    if len(inputNombre > 50):
         raise forms.ValidationError("El largo maximo es de 50 caracteres")
    return inputNombre

        

