from django.http import HttpResponse 
from django.shortcuts import render
 
import datetime


class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

        


def saludo(request): #primera vista 

    usuario1 = Persona("Tomas", "Artaza")
    temas_DelCurso = ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    #temas_DelCurso = []

    #nombre = "Tomy" 
    #apellido = "Artaza"
    tiempo = datetime.datetime.now() 
 
   # doc_externo = open("C:/Users/tomas/OneDrive/Escritorio/Progamation/ProyectoDjango/Proyecto1/Proyecto1/Plantillas/plantilla.html") #abro el docu
   # plt = Template(doc_externo.read()) #lo leo
   # doc_externo.close() #cierro el docu

   # contexto = Context({"nombre_persona": usuario1.nombre, "apellido_persona":usuario1.apellido, "hora_actual":tiempo, "temas":temas_DelCurso}) #le doy un panorama, datos adicionales al template

   # documento = plt.render(contexto) #renderizo el objeto template 

    return render(request, "plantilla.html",{"nombre_persona": usuario1.nombre, "apellido_persona":usuario1.apellido, "hora_actual":tiempo, "temas":temas_DelCurso})

def despedida(request):
    return HttpResponse("Nos vimo perrito malvado") 

def dameFecha(request):
    fecha_actual = datetime.datetime.now() 

    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    <h1>
    <body>
    <html> """ % fecha_actual

    return HttpResponse(documento) 

def calculaEdad(request, anio, edad):
    
    periodo = anio - 2020
    edadFutura = edad + periodo

    documento = "<html> <body> <h2> En el año %s tendras %s años" %(anio, edadFutura)

    return HttpResponse(documento) 

def theOffice(request):
    return render(request, "theOffice.html") 

def theOffice_reparto(request):
    return render(request, "reparto.html") 