from django.db import models

from apps.users.models import User


class Equipment(models.Model):
    STATUS_CHOICES = [
        ("operational", "operational"),
        ("under_maintenance", "under maintenance"),
    ]
    equipment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    purchase_date = models.DateField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    last_maintenance_date = models.DateField()

    def __str__(self):
        return self.name

class Maintenance(models.Model):
    maintenance_id = models.AutoField(primary_key=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    maintenance_date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.equipment.name} - {self.maintenance_date}"

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.email}"
