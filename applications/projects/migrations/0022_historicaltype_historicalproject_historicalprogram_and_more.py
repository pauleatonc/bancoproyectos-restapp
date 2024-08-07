# Generated by Django 4.2.2 on 2023-10-03 19:07

import applications.projects.functions
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('regioncomuna', '0003_crear_comuna_generica'),
        ('projects', '0021_remove_historicalprogram_history_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalType',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Tipo de Proyecto')),
                ('icon_type', models.CharField(default='other_admission', max_length=200, verbose_name='Icono ( Nombre icono)')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('program', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.program', verbose_name='Programa (obligatorio)')),
            ],
            options={
                'verbose_name': 'historical Tipo',
                'verbose_name_plural': 'historical Tipos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProject',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Nombre (obligatorio)')),
                ('id_subdere', models.CharField(db_index=True, max_length=200, verbose_name='ID SUBDERE (obligatorio)')),
                ('description', models.TextField(verbose_name='Descripción (obligatorio)')),
                ('public', models.BooleanField(default=True)),
                ('video', models.CharField(blank=True, max_length=200, null=True, verbose_name='Youtube')),
                ('portada', models.CharField(max_length=100, null=True, verbose_name='Foto portada (obligatorio)')),
                ('beforeimage', models.CharField(blank=True, max_length=100, null=True, verbose_name='Imagen Antes')),
                ('afterimage', models.CharField(blank=True, max_length=100, null=True, verbose_name='Imagen Después')),
                ('eett', models.CharField(max_length=100, null=True, validators=[django.core.validators.FileExtensionValidator(['pdf'], message='Solo se permiten archivos PDF.'), applications.projects.functions.validate_file_size_five], verbose_name='EETT')),
                ('presupuesto', models.CharField(max_length=100, null=True, validators=[django.core.validators.FileExtensionValidator(['pdf'], message='Solo se permiten archivos PDF.'), applications.projects.functions.validate_file_size_five], verbose_name='Presupuesto')),
                ('planimetria', models.CharField(max_length=100, null=True, validators=[applications.projects.functions.validate_file_size_twenty], verbose_name='Planimetría')),
                ('slug', models.SlugField(editable=False, max_length=300)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('comuna', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='regioncomuna.comuna', verbose_name='Comuna')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('program', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.program', verbose_name='Programa (obligatorio)')),
                ('type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.type', verbose_name='Tipo de Proyecto (obligatorio)')),
                ('year', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.year', verbose_name='Año (obligatorio)')),
            ],
            options={
                'verbose_name': 'historical Proyecto',
                'verbose_name_plural': 'historical Proyectos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProgram',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Nombre')),
                ('sigla', models.CharField(db_index=True, max_length=200, verbose_name='Sigla')),
                ('icon_program', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Programa',
                'verbose_name_plural': 'historical Programas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPrioritizedTag',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('prioritized_tag', models.CharField(db_index=True, max_length=20, verbose_name='Tag para proyectos priorizados')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Tag priorizado',
                'verbose_name_plural': 'historical Tags priorizados',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
