from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=15, unique=True)
    # descripcion = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Categoría de Produecto"
        verbose_name_plural = "Categorías de Productos"