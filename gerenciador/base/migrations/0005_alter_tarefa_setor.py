# Generated by Django 4.1.5 on 2023-01-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_pessoas_options_alter_tarefa_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='setor',
            field=models.CharField(choices=[('Produção', 'Produção'), ('Financeiro', 'Financeiro'), ('Logística', 'Logística'), ('Engenharia', 'Engenharia'), ('Manutenção', 'Manutenção'), ('Administração', 'Administração'), ('Recursos Humanos', 'Recursos Humanos')], max_length=50, verbose_name='Setor'),
        ),
    ]
