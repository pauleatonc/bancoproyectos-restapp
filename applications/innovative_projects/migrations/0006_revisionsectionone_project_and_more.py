# Generated by Django 4.2.2 on 2023-09-26 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('innovative_projects', '0005_remove_revisionsectionone_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='revisionsectionone',
            name='project',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revision_section_one', to='innovative_projects.innovativeprojects'),
        ),
        migrations.AddField(
            model_name='revisionsectiontwo',
            name='project',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revision_section_two', to='innovative_projects.innovativeprojects'),
        ),
    ]
