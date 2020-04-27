# Generated by Django 3.0.3 on 2020-02-13 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arts_core', '0007_runtime_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='args',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='module',
            name='filename',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='parent',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='arts_core.Runtime'),
            preserve_default=False,
        ),
    ]
