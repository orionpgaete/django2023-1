
import datetime
from django.http import HttpResponse
from django.template import Template, Context


def saludo(request):
    return HttpResponse("Hola a todos")

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        pass


def plantilla(request):
    doc_externo = open("D:/1. Clases INACAP/2. Clases/2.31 Programacion Back-End/Proyectos 2023/Proyecto_1/Proyecto_1/plantilla/miplantilla.html")
    
    plt = Template(doc_externo.read())

    doc_externo.close()

    nombre = "Andres"
    apellido = "Perez"

    p1=Persona("Pablo","Martinez")

    fecha_actual = datetime.datetime.now()

    temascurso=["Modelos", "Vistas", "Formularios", "Despliegues"]

    ctx = Context({"nombre_persona" : p1.nombre, "apellido_persona": p1.apellido, "fecha": fecha_actual, "temas":temascurso})

    pagina = plt.render(ctx)

    return HttpResponse(pagina)
