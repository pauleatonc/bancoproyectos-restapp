# Generated by Django 4.1.3 on 2023-06-30 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tipo_usuario',
            field=models.CharField(choices=[('SUBDERE', 'SUBDERE'), ('BANCO', 'Banco de Proyectos')], default='BANCO', max_length=20, verbose_name='SUBDERE o Banco de Proyectos'),
        ),
    ]
