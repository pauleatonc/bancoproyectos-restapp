# Generated by Django 4.2.2 on 2023-10-19 12:17

import applications.users.functions
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_historicaltype_historicalproject_historicalprogram_and_more'),
        ('users', '0007_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalUser',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('rut', models.CharField(db_index=True, max_length=15, validators=[applications.users.functions.validar_rut])),
                ('nombres', models.CharField(blank=True, max_length=30, null=True)),
                ('primer_apellido', models.CharField(blank=True, max_length=30, null=True)),
                ('segundo_apellido', models.CharField(blank=True, max_length=30, null=True)),
                ('comuna', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=200)),
                ('email', models.TextField(blank=True, max_length=100, null=True)),
                ('institucion', models.CharField(blank=True, max_length=50, null=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='Usuario administrador')),
                ('is_active', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('program', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='projects.program', verbose_name='Programa')),
            ],
            options={
                'verbose_name': 'historical Usuario',
                'verbose_name_plural': 'historical Usuarios',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
