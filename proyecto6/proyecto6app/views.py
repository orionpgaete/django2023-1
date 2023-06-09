from django.shortcuts import render
from proyecto6app.forms import FormProyecto
from proyecto6app.models import Proyecto

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listaproyecto(request):
    proyecto = Proyecto.objects.all()
    data = {'proyectos': proyecto}
    return render(request, 'proyecto.html', data)

def agregarproyecto(request):
    form = FormProyecto()
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarproyecto.html', data)

