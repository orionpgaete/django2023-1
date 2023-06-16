from django.shortcuts import redirect, render
from proyecto6app.forms import FormProyecto, IngresoForm
from proyecto6app.models import Proyecto

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listaproyecto(request):
    proyecto = Proyecto.objects.all()
    data = {'proyectos': proyecto}
    return render(request, 'proyecto.html', data)

def agregarproyecto(request):
    form = IngresoForm()
    if request.method == 'POST':
        #form = FormProyecto(request.POST)
        form = IngresoForm(request.POST)
        if form.is_valid() :
            proyecto = Proyecto()
            proyecto.nombre = form.cleaned_data['nombre']
            proyecto.prioriodad = form.cleaned_data['prioridad']
            proyecto.responsable = form.cleaned_data['responsable']
            proyecto.fechaInicio = form.cleaned_data['fechaInicio']
            proyecto.fechaTermino = form.cleaned_data['fechaTermino']
            proyecto.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarproyecto.html', data)

def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    proyecto.delete()
    return redirect('/lista')


def modificaProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    form = FormProyecto(instance=proyecto)

    if request.method == 'POST':
        form = FormProyecto(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarproyecto.html', data)



