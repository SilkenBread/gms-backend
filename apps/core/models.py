from django.db import models


# Create your models here.
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    DAY_CHOICES = [
        ("monday", "Lunes"),
        ("tuesday", "Martes"),
        ("wednesday", "Miércoles"),
        ("thursday", "Jueves"),
        ("friday", "Viernes"),
        ("saturday", "Sábado"),
        ("sunday", "Domingo"),
    ]

    day = models.CharField(max_length=30, choices=DAY_CHOICES)

    DAY_CATEGORY_CHOICES = [
        ("morning", "mañana"),
        ("afternoon", "tarde"),
        ("evening", "noche")
    ]

    day_category = models.CharField(max_length=30, choices=DAY_CATEGORY_CHOICES)