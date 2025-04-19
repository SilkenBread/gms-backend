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
            name='Member',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birth_date', models.DateField()),
                ('registration_date', models.DateField()),
                ('active_membership', models.BooleanField(default=True)),
                ('membership_type', models.CharField(choices=[('monthly', 'monthly'), ('annual', 'annual')], max_length=20)),
                ('membership_end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('entry_time', models.DateTimeField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('payment_method', models.CharField(choices=[('cash', 'cash'), ('transfer', 'transfer')], max_length=20)),
                ('period', models.CharField(choices=[('monthly', 'monthly'), ('annual', 'annual')], max_length=20)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalEvaluation',
            fields=[
                ('evaluation_id', models.AutoField(primary_key=True, serialize=False)),
                ('evaluation_date', models.DateField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('notes', models.TextField(blank=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
    ]
