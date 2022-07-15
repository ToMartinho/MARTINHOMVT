from django.http import HttpResponse
from django.shortcuts import render

from AppMVT.models import Familiares

# Create your views here.
def agrega_familiar(self, tipo_f, nombre, apellido, edad, estado_f):

    familiar = Familiares(tipo_f=tipo_f, nombre=nombre, apellido=apellido, edad=edad, estado_f=estado_f)
    familiar.save()

    return HttpResponse(f"""
            <p>El familiar tipo: {familiar.tipo_f} con nombre y apellido: {familiar.nombre} {familiar.apellido} edad: {familiar.edad} y estado: {familiar.estado_f} se agrego a la DB</p>
    """)