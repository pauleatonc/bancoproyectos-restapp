# Generated by Django 4.2.2 on 2023-09-28 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_historicalprogram_guide_historicaltype_program_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklistdocuments',
            name='state',
        ),
        migrations.RemoveField(
            model_name='guide',
            name='state',
        ),
        migrations.RemoveField(
            model_name='historicalchecklistdocuments',
            name='state',
        ),
        migrations.RemoveField(
            model_name='historicalguide',
            name='state',
        ),
        migrations.RemoveField(
            model_name='historicalprioritizedtag',
            name='state',
        ),
        migrations.RemoveField(
            model_name='historicalprogram',
            name='state',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='state',
        ),
        migrations.RemoveField(
            model_name='historicaltype',
            name='state',
        ),
        migrations.RemoveField(
            model_name='prioritizedtag',
            name='state',
        ),
        migrations.RemoveField(
            model_name='program',
            name='state',
        ),
        migrations.RemoveField(
            model_name='project',
            name='state',
        ),
        migrations.RemoveField(
            model_name='type',
            name='state',
        ),
    ]
