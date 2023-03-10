# Generated by Django 4.1.5 on 2023-01-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_pessoas_alter_tarefa_responsavel'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoas',
            name='cargo',
            field=models.CharField(choices=[('Gerente', 'Gerente'), ('Supervisor', 'Supervisor'), ('Coordenador', 'Coordenador'), ('Diretor', 'Diretor'), ('Operador', 'Operador')], default='Outros', max_length=50, verbose_name='Cargo'),
        ),
        migrations.AddField(
            model_name='pessoas',
            name='setor',
            field=models.CharField(choices=[('Produção', 'Produção'), ('Financeiro', 'Financeiro'), ('Logística', 'Logística'), ('Engenharia', 'Engenharia'), ('Manutenção', 'Manutenção'), ('Administração', 'Administração'), ('Recursos Humanos', 'Recursos Humanos')], default='Outros', max_length=50, verbose_name='Setor'),
        ),
    ]
