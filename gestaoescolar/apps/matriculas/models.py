from django.db import models
from django.db import models
from alunos.models import Aluno
from turmas.models import Turma

# Create your models here.

class Matricula(models.Model):
    data_matricula = models.DateTimeField('Data da matrícula', auto_now_add=True)
    status = models.CharField('Status', max_length=50)

    nota1 = models.DecimalField('Nota 1', max_digits=5, decimal_places=2, default=0)
    nota2 = models.DecimalField('Nota 2', max_digits=5, decimal_places=2, default=0)
    nota_final = models.DecimalField('Nota final', max_digits=5, decimal_places=2, default=0)
    media_final = models.DecimalField('Média final', max_digits=5, decimal_places=2, default=0)
    frequencia = models.DecimalField('Frequência', max_digits=5, decimal_places=2, default=0)

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'
        ordering = ['id']

    def __str__(self):
        return f"Matrícula de {self.aluno.nome_completo} na turma {self.turma.nome}"