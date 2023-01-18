from django.db import models

# Create your models here.

class Pessoas(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Colaborador')


class Tarefa(models.Model):
    LISTA_STATUS = (
        ('Fechado', 'Fechado'),
        ('Pendente','Pendente'),
        ('Em Progresso', 'Em Progresso'),
    )

    responsavel = models.ForeignKey(Pessoas, verbose_name="Quem?", on_delete=models.CASCADE)
    tarefa = models.CharField(max_length=100, verbose_name="O que?")
    data = models.DateField(verbose_name='Quando?')
    status = models.CharField(max_length=20, verbose_name='Status', choices=LISTA_STATUS)
