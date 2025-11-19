from django.db import models

class Area(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição')
    coordenador = models.CharField('Coordenador', max_length=100)

    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'
        ordering = ['id']

    def __str__(self):
        return self.nome
