# Generated by Django 5.0.7 on 2024-08-01 02:04

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_feedback_satisfactionsurvey'),
    ]

    operations = [
        migrations.CreateModel(
            name='Behavior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('absenteeism_days', models.PositiveIntegerField(default=0)),
                ('overtime_hours', models.PositiveIntegerField(default=0)),
                ('training_engagement', models.FloatField(default=0.0)),
                ('notes', models.TextField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.employee')),
            ],
        ),
    ]
