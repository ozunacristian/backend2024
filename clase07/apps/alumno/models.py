from django.db import models

# Create your models here.
class Alumno(models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  dni = models.CharField(max_length=8)
  fecha_nacimiento = models.DateField()
  direccion = models.CharField(max_length=100)
  telefono = models.CharField(max_length=20)
  email = models.EmailField()
  activo = models.BooleanField(default=True)

  def __str__(self):
    return f"{self.nombre} {self.apellido}"
