# servicios/models.py
from django.db import models

class Servicio(models.Model):
    precio = models.IntegerField()
    foto = models.ImageField(upload_to='servicios/')
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion
