from django.contrib.auth.models import Group
from django.db import migrations


def create_employee_groups(apps, schema_editor):
    Group.objects.get_or_create(name="administrator")
    Group.objects.get_or_create(name="trainer")
    Group.objects.get_or_create(name="receptionist")

class Migration(migrations.Migration):
    dependencies = [
        ("employees", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_employee_groups),
    ]
