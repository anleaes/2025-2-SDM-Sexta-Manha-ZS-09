from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome_completo = models.CharField('Nome completo', max_length=150)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    data_nascimento = models.DateField('Data de nascimento')
    email = models.EmailField('Email', max_length=150)
    telefone = models.CharField('Telefone', max_length=20)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['id']

    def __str__(self):
        return self.nome_completo