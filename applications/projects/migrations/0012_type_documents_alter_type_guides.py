# Generated by Django 4.2.2 on 2023-09-05 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_alter_documents_title_and_more'),
        ('projects', '0011_remove_innovativegaleryimage_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='documents',
            field=models.ManyToManyField(blank=True, related_name='documents', to='documents.documents'),
        ),
        migrations.AlterField(
            model_name='type',
            name='guides',
            field=models.ManyToManyField(blank=True, related_name='guides', to='projects.guide'),
        ),
    ]
