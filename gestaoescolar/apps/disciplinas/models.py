from django.db import models
from areas.models import Area

# Create your models here.

class Disciplina(models.Model):
    codigo = models.CharField('Código', max_length=20)
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição')
    carga_horaria = models.IntegerField('Carga Horária')
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ['id']

    def __str__(self):
        return f"{self.codigo} - {self.nome}"