
from django.urls import path
from .views import listar_servicios

urlpatterns = [
    path('nuestros-servicios/', listar_servicios, name='listar_servicios'),
]
