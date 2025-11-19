from django.db import models
from areas.models import Area
# Create your models here.

class Curso(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição')
    carga_horaria_total = models.IntegerField('Carga Horária Total')
    nivel = models.CharField('Nível', max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']

    def __str__(self):
        return self.nome