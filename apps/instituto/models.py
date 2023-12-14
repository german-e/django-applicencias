from django.db import models


class Instituto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=50, default='Chaco')
    email = models.EmailField()
    telefono = models.CharField(max_length=25)
    cuof = models.CharField(max_length=10)
    cue = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.nombre}'
    
    class Meta:
        db_table = 'Instituciones'


"""
class Carrera(models.Model):
    nombre_completo,
    nombre_corto,
    duracion
    activo
    observaciones,
"""







"""
instituto
carrera
materias
cargos
docentes

movimientos
    id    
    desde
    hasta
    docente_id
    instumento_legal


licencia_hs
    movimiento_id
    materia
    cargo

alta
    movimineto_id
    materia_id
    cargo_id
    sit_revista
    doc_reemplazado
    mov_licencia_id


"""