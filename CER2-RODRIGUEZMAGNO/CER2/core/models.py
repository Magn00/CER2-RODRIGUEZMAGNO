from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario.username

class Profesor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario.username

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tematica = models.CharField(max_length=100, default='General')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    patrocinado = models.BooleanField(default=False)
    profesor = models.ForeignKey(Profesor, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.titulo

