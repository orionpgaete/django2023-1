from django.shortcuts import render
from proyecto5app.models import Empleados
from . import forms
# Create your views here.

def empleadosData(request):
    persona = Empleados.objects.all()
    data = {'personas': persona}
    return render(request, 'empleados.html', data)

def empleadosform(request):
    form = forms.empleadosform()
    data = {'formu' : form}
    return render(request, 'registro.html', data)
