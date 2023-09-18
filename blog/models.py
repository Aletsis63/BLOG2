from django.db import models
from django.urls import reverse

# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=32)
    autor = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    cuerpo = models.TextField()

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        #representa el nombre de la url
        return reverse('detalle_pub', kwargs={'pk': self.pk})
    