from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User


class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    estado = models.CharField(
        max_length=20,
        choices=[
            ('activo', 'Activo'),
            ('reparacion', 'Reparación'),
            ('baja', 'Baja'),
        ]
    )

    ubicacion = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Perfil(models.Model):

    ROLES = (
        ('admin', 'Administrador'),
        ('tecnico', 'Técnico'),
        ('auditor', 'Auditor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return self.user.username
    
