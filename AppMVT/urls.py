from django.contrib import admin
from django.urls import path
from AppMVT.views import agrega_familiar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agrega-familiar/<tipo_f>/<nombre>/<apellido>/<edad>/<estado>', agrega_familiar),
]
