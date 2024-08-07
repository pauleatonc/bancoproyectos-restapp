# Generated by Django 4.2.2 on 2023-09-06 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regioncomuna', '0002_rename_nombre_comuna_comuna_and_more'),
        ('projects', '0012_type_documents_alter_type_guides'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectimage',
            old_name='image_carousel',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='project',
            name='comuna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='regioncomuna.comuna', verbose_name='Comuna'),
        ),
    ]
