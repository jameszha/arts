# Generated by Django 3.0.3 on 2020-06-22 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts_core', '0023_module_channels'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='env',
            field=models.CharField(blank=True, default=[''], max_length=1000),
        ),
        migrations.AlterField(
            model_name='module',
            name='args',
            field=models.CharField(blank=True, default=[''], max_length=1000),
        ),
    ]
