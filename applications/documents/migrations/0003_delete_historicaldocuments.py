# Generated by Django 4.2.2 on 2023-09-20 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_alter_documents_title_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricalDocuments',
        ),
    ]
