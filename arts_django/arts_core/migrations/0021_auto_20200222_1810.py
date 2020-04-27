# Generated by Django 3.0.3 on 2020-02-22 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts_core', '0020_auto_20200219_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runtime',
            name='apis',
            field=models.CharField(blank=True, default=['wasi:snapshot_preview1', 'wasi:unstable', 'wasi:core', 'wasi:clock', 'wasi:environ', 'wasi:sock', 'wasi:args', 'wasi:fd', 'wasi:path', 'wasi:poll', 'wasi:proc', 'wasi:random', 'wasi:sched', 'wasi:sock', 'python:core'], max_length=500),
        ),
    ]
