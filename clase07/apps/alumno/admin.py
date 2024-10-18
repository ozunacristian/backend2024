from django.contrib import admin
from apps.alumno.models import Alumno

# Register your models here.
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
  list_display = [nombre, apellido, dni, fecha_nacimiento, direccion, telefono, email, activo,]
  search_fields = [nombre, apellido, fecha_nacimiento, email, activo,]
  list_filter = []