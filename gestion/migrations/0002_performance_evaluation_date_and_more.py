# Generated by Django 5.0.7 on 2024-08-01 01:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='evaluation_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='performance_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='promotion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='performance',
            name='salary_increase',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
