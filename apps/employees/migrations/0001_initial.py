# Generated by Django 5.1.6 on 2025-04-19 00:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_rename_first_name_user_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('position', models.CharField(choices=[('trainer', 'trainer'), ('receptionist', 'receptionist')], max_length=50)),
                ('hire_date', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('purchase_date', models.DateField()),
                ('status', models.CharField(choices=[('operational', 'operational'), ('under_maintenance', 'under maintenance')], max_length=30)),
                ('last_maintenance_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('maintenance_id', models.AutoField(primary_key=True, serialize=False)),
                ('maintenance_date', models.DateField()),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.equipment')),
            ],
        ),
    ]
