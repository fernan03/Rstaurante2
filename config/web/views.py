from django.shortcuts import render

from web.formularios.formularioPlato import FormularioPlatos

from web.formularios.formularioEmpleados import FormularioEmpleados

from web.models import Platos

from web.models import Empleados

# Create your views here.

#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request,'home.html')

def PlatosVista(request):
    #esta vista va a itulizar un formulario de django
    #debo crear entonces un objeto de la CLASE FormularioPlatos()
    formulario=FormularioPlatos()

    #Creamos un diccionario para enviar el formulario al HTML(TEMPLATE)
    data={
        'formulario':formulario
    }
    #RECIBIMOS LOS DATOS DEL FORMULARIO
    if request.method=="POST":
        datosFormulario=FormularioPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            print(datosLimpios)
            #CONTRUIR UN DICCIONARIO DE ENVIO DE DATOS HACIA LA BD
            platoNuevo=Platos(
                nombre=datosLimpios["nombre"],
                descripcion=datosLimpios["descripcion"],
                fotografia=datosLimpios["fotografia"],
                precio=datosLimpios["precio"],
                tipo=datosLimpios["tipo"]
            )
            #INTENTARE LLEVAR MIS DATOS A LA BASE DE DATOS
            try:
                platoNuevo.save()
                print("Exito guardando....")
            except Exception as error:
                print("upsss", error)


    return render(request,'menuplatos.html',data)

def EmpleadosVista(request):
    formulario=FormularioEmpleados()
    data={
        'formulario':formulario
    }
    if request.method=="POST":
        datosFormulario=FormularioEmpleados(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            print(datosLimpios)

            empleadoNuevo=Empleados(
                nombre=datosLimpios["nombre"],
                apellido=datosLimpios["apellido"],
                fotografia=datosLimpios["fotografia"],
                tipo=datosLimpios["tipo"],
                salario=datosLimpios["salario"],
                contacto=datosLimpios["contacto"]
            )
            try:
                empleadoNuevo.save()
                print("Exito guardando")
            except Exception as error:
                print("upsss", error)
    return render(request,'registrarEmpleados.html',data)
