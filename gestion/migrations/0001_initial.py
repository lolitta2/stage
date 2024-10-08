# Generated by Django 5.0.7 on 2024-07-31 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('photo_url', models.URLField(blank=True, max_length=255, null=True)),
                ('position', models.CharField(max_length=100)),
                ('department', models.CharField(default='Unknown', max_length=100)),
                ('hire_date', models.DateField()),
                ('employment_status', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contractual', 'Contractual')], max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='AdministrativeInfo',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gestion.employee')),
                ('employee_number', models.CharField(blank=True, max_length=20, null=True)),
                ('social_security_number', models.CharField(blank=True, max_length=20, null=True)),
                ('employment_status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('On leave', 'On leave'), ('Terminated', 'Terminated')], max_length=20, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gestion.employee')),
                ('health_insurance', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True)),
                ('retirement_plan', models.CharField(blank=True, choices=[('401k', '401k'), ('Pension', 'Pension'), ('None', 'None')], max_length=10, null=True)),
                ('other_benefits', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentTermination',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gestion.employee')),
                ('termination_date', models.DateField(blank=True, null=True)),
                ('termination_reason', models.CharField(blank=True, choices=[('Resignation', 'Resignation'), ('Layoff', 'Layoff'), ('Termination', 'Termination'), ('Retirement', 'Retirement'), ('Other', 'Other')], max_length=20, null=True)),
                ('non_compete_clause', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HealthAndSafety',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gestion.employee')),
                ('medical_conditions', models.TextField(blank=True, null=True)),
                ('work_accident_history', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gestion.employee')),
                ('performance_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('goals', models.TextField(blank=True, null=True)),
                ('development_plan', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('work_hours', models.TimeField(blank=True, null=True)),
                ('overtime_hours', models.TimeField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('leave_id', models.AutoField(primary_key=True, serialize=False)),
                ('leave_type', models.CharField(blank=True, choices=[('Vacation', 'Vacation'), ('Sick leave', 'Sick leave'), ('Parental leave', 'Parental leave'), ('Other', 'Other')], max_length=20, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gestion.employee')),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('hire_date', models.DateField(blank=True, null=True)),
                ('employment_status', models.CharField(blank=True, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contractual', 'Contractual')], max_length=20, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinates', to='gestion.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(blank=True, max_length=100, null=True)),
                ('training_course', models.CharField(max_length=100)),
                ('skill', models.CharField(blank=True, max_length=100, null=True)),
                ('performance_review', models.TextField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.employee')),
            ],
            options={
                'unique_together': {('employee', 'training_course')},
            },
        ),
    ]
