# Generated by Django 5.0.6 on 2024-06-03 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_proyecto_profesor_proyecto_tematica_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='matricula',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='departamento',
        ),
    ]
