from django.shortcuts import render

from web.formularios.formularioPlato import FormularioPlatos

from web.formularios.formularioEmpleados import FormularioEmpleados

# Create your views here.

#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request,'home.html')

def Platos(request):
    #esta vista va a itulizar un formulario de django
    #debo crear entonces un objeto de la CLASE FormularioPlatos()
    formulario=FormularioPlatos()

    #Creamos un diccionario para enviar el formulario al HTML(TEMPLATE)
    data={
        'formulario':formulario
    }
    return render(request,'menuplatos.html',data)

def Empleados(request):
    formulario=FormularioEmpleados()
    data={
        'formulario':formulario
    }
    return render(request,'registrarEmpleados.html',data)
