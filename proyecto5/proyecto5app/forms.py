from django import forms

class empleadosform(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    fono = forms.CharField()