from django.db import models

# Create your models here.
class Cursada(models.Model):
  alumno = models.ForeignKey("alumno.Alumno", on_delete=models.CASCADE)
  carrera = models.ForeignKey("carrera.Carrera", on_delete=models.CASCADE)
  fecha_inscripcion=models.DateField()
  activa=models.BooleanField(default=True)

  def __str__(self):
    return f"{self.alumno} {self.carrera}"
