from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'template/index.html')

def rendertemplate(request):
    data = {"nombre": "Pedro"}
    return render(request, 'template/plantilla.html', data)

def renderinfo(request):
    data = {"id": "123", "nombre": "Pedro Gaete", "email": "pedro@gmail.com" }
    return render(request, 'template/userInfoTemplate.html', data)

