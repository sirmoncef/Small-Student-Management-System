# Generated by Django 5.0.4 on 2024-04-23 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stmapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Departement',
            field=models.CharField(choices=[('Preparatory Cycle', 'CP'), ('Super Cycle', 'CS')], max_length=50),
        ),
    ]
