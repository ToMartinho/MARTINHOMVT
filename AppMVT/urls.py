from django.contrib import admin
from django.urls import path
from AppMVT.views import agrega_familiar

urlpatterns = [
        path('agrega-familiar/<tipo_f>/<nombre>/<apellido>/<edad>/<estado_f>/', agrega_familiar),
]
