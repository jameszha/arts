# Generated by Django 3.0.3 on 2020-02-14 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts_core', '0010_auto_20200214_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='filename',
            field=models.CharField(max_length=255),
        ),
    ]
