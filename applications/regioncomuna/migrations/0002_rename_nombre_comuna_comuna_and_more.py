# Generated by Django 4.2.2 on 2023-07-31 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regioncomuna', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comuna',
            old_name='nombre',
            new_name='comuna',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='nombre',
            new_name='region',
        ),
    ]