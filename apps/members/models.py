from django.db import models

from apps.users.models import User


class Member(models.Model):
    MEMBERSHIP_TYPE_CHOICES = [
        ("monthly", "monthly"),
        ("annual", "annual"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birth_date = models.DateField()
    registration_date = models.DateField()
    active_membership = models.BooleanField(default=True)
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_TYPE_CHOICES)
    membership_end_date = models.DateField()

    def __str__(self):
        return f"{self.user.email} - {self.membership_type}"

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ("cash", "cash"),
        ("transfer", "transfer"),
    ]
    PERIOD_CHOICES = [
        ("monthly", "monthly"),
        ("annual", "annual"),
    ]
    payment_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES)

    def __str__(self):
        return f"{self.member.user.email} - {self.amount} ({self.payment_date})"

class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    entry_time = models.DateTimeField()

    def __str__(self):
        return f"{self.member.user.email} - {self.entry_time}"

class PhysicalEvaluation(models.Model):
    evaluation_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    evaluation_date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.member.user.email} - {self.evaluation_date}"
