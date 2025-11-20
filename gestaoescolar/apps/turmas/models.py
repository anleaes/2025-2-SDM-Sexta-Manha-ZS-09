from django.db import models
from professores.models import Professor
from disciplinas.models import Disciplina
from curso.models import Curso
from campus.models import Campus
from salas.models import Sala

# Create your models here.

class Turma(models.Model):
    nome = models.CharField('Nome da turma', max_length=150)
    capacidade = models.IntegerField('Capacidade')
    data_inicio = models.DateField('Data de início')
    data_fim = models.DateField('Data de fim')
    status = models.CharField('Status', max_length=50)

    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['id']

    def __str__(self):
        return self.nome