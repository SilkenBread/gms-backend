# Generated by Django 5.1.6 on 2025-04-19 00:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='surname',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('employee', 'employee'), ('member', 'member')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID number'),
        ),
    ]
