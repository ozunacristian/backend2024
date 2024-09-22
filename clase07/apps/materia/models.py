from django.db import models

# Create your models here.
class Materia(models.Model):
  nombre = models.CharField(max_length=50)
  carrera = models.ForeignKey("carrera.Carrera", on_delete=models.CASCADE)

  def __str__(self):
    return {self.nombre}
