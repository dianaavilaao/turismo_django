
from django.shortcuts import render
from .models import Servicio

def listar_servicios(request):
    servicios = Servicio.objects.raw('SELECT * FROM servicios_servicio')
    return render(request, 'servicios/listar.html', {'servicios': servicios})
