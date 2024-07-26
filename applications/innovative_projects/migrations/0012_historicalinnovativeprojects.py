# Generated by Django 4.2.2 on 2023-10-03 19:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0021_remove_historicalprogram_history_user_and_more'),
        ('innovative_projects', '0011_delete_historicalinnovativeprojects'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalInnovativeProjects',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('title', models.CharField(blank=True, db_index=True, max_length=23, verbose_name='Título (obligatorio)')),
                ('description', models.TextField(blank=True, validators=[django.core.validators.MinLengthValidator(280, 'La descripción debe tener al menos 280 caracteres.')])),
                ('portada', models.CharField(blank=True, max_length=100, null=True, verbose_name='Foto portada (obligatorio)')),
                ('public', models.BooleanField(default=False)),
                ('request_sent', models.BooleanField(default=False)),
                ('evaluated', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('program', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.program', verbose_name='Programa (obligatorio)')),
            ],
            options={
                'verbose_name': 'historical Proyecto Innovador',
                'verbose_name_plural': 'historical Proyectos Innovadores',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
