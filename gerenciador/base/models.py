from django.db import models

# Create your models here.

class Pessoas(models.Model):
    
    LISTA_CARGOS = (
        ('Gerente', 'Gerente'),
        ('Supervisor', 'Supervisor'),
        ('Coordenador', 'Coordenador'),
        ('Diretor', 'Diretor'),
        ('Operador', 'Operador')
    )
    nome = models.CharField(max_length=50, verbose_name='Colaborador')
    cargo = models.CharField(max_length=50, verbose_name='Cargo', choices=LISTA_CARGOS, default='Outros')

    def __str__(self):
        return f'{self.nome}'
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['nome']


class Tarefa(models.Model):
    LISTA_STATUS = (
        ('Feito', 'Feito'),
        ('Em Progresso', 'Em Progresso'),
        ('Pendente','Pendente'),
        
    )
    LISTA_SETOR = (
        ('Produção', 'Produção'),
        ('Financeiro', 'Financeiro'),
        ('Logística', 'Logística'),
        ('Engenharia', 'Engenharia'),
        ('Manutenção', 'Manutenção'),
        ('Administração', 'Administração'),
        ('Recursos Humanos', 'Recursos Humanos')
    )

    responsavel = models.ForeignKey(Pessoas, verbose_name="Quem?", on_delete=models.CASCADE)
    setor = models.CharField(max_length=50, verbose_name='Setor', choices=LISTA_SETOR)
    tarefa = models.CharField(max_length=100, verbose_name="O que?")
    data = models.DateField(verbose_name='Quando?')
    status = models.CharField(max_length=20, verbose_name='Status', choices=LISTA_STATUS)

    def __str__(self):
            return f'{self.responsavel}'
    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['-data']