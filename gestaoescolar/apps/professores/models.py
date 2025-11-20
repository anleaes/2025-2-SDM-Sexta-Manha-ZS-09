from django.db import models

# Create your models here.


class Professor(models.Model):
    nome_completo = models.CharField('Nome completo', max_length=150)
    matricula_funcional = models.CharField('Matrícula funcional', max_length=50, unique=True)
    data_contratacao = models.DateField('Data de contratação')
    email = models.EmailField('Email', max_length=120)
    valor_hora = models.DecimalField('Valor hora', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ['id']

    def __str__(self):
        return self.nome_completo
