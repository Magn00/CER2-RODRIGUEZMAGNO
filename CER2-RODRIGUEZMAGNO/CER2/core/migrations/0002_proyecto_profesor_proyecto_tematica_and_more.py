# Generated by Django 5.0.6 on 2024-06-03 05:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.profesor'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='tematica',
            field=models.CharField(default='General', max_length=100),
        ),
        migrations.DeleteModel(
            name='Patrocinio',
        ),
    ]
