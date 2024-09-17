from django.db import models

# Create your models here.
class Carrera(models.Model):
  nombre = models.CharField(max_length=50)
  duración = models.PositiveIntegerField()
  activa = models.BooleanField(default=True)

  def __str__(self):
    return self.nombre