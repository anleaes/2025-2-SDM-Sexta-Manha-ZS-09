from django.db import models

# Create your models here.

class Campus(models.Model):
    nome = models.CharField('Nome', max_length=150)
    endereco = models.TextField('Endereço')
    cidade = models.CharField('Cidade', max_length=100)
    uf = models.CharField('UF', max_length=2)

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campi'
        ordering = ['id']

    def __str__(self):
        return self.nome