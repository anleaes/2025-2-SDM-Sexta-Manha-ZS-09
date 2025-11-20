from django.db import models

# Create your models here.

class Sala(models.Model):
    numero_sala = models.CharField('Número da sala', max_length=50)
    predio = models.CharField('Prédio', max_length=100)
    tipo = models.CharField('Tipo', max_length=100)
    quantidade_lugares = models.IntegerField('Quantidade de lugares')

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        ordering = ['id']

    def __str__(self):
        return f"{self.numero_sala} - {self.predio}"
