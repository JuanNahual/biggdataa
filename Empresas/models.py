from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    rubro = models.CharField(max_length=100, choices=[
        ('tecnologia', 'Tecnología'),
        ('salud', 'Salud'),
        ('comida', 'Comida'),
        ('educacion', 'Educación'),
    ])
    descripcion = models.TextField()
    website = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='empresas/', blank=True, null=True)  # Nuevo campo para la imagen

    def __str__(self):
        return self.nombre