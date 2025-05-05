from django.db import models
from apps.users.models import User
from datetime import timedelta
from django.utils import timezone


class MembershipPlan(models.Model):
    DURATION_CHOICES = [
        ('days', 'Días'),
        ('months', 'Meses'),
        ('years', 'Años')
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField()
    duration_unit = models.CharField(max_length=10, choices=DURATION_CHOICES)
    validity = models.PositiveIntegerField(help_text="Tiempo que el plan está activo para ser comprado (días)")
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Plan de Membresía"
        verbose_name_plural = "Planes de Membresía"

    def __str__(self):
        return f"{self.name} - ${self.price}"

    def calculate_end_date(self, from_date=None):
        from_date = from_date or timezone.now().date()
        
        if self.duration_unit == 'days':
            return from_date + timedelta(days=self.duration)
        elif self.duration_unit == 'months':
            return from_date + timedelta(days=30 * self.duration)
        elif self.duration_unit == 'years':
            return from_date + timedelta(days=365 * self.duration)
        return from_date


class Member(models.Model):
    MEMBERSHIP_TYPE_CHOICES = [
        ("monthly", "monthly"),
        ("annual", "annual"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birth_date = models.DateField()
    registration_date = models.DateField()
    active_membership = models.BooleanField(default=True)
    membership_plan = models.ForeignKey(
        MembershipPlan, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    membership_start_date = models.DateField(null=True, blank=True)
    membership_end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.membership_plan.name if self.membership_plan else 'Sin plan'}"
    
    def update_membership(self, plan, payment_date=None):
        self.membership_plan = plan
        self.membership_start_date = payment_date or timezone.now().date()
        self.membership_end_date = plan.calculate_end_date(self.membership_start_date)
        self.active_membership = True
        self.save()

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Efectivo'),
        ('transfer', 'Transferencia'),
        ('card', 'Tarjeta')
    ]

    payment_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='payments')
    membership_plan = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='created_payments'
    )

    class Meta:
        ordering = ['-payment_date']
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return f"Pago #{self.payment_id} - {self.member.user.get_full_name()}"

    def save(self, *args, **kwargs):
        # Asegurar que el monto coincide con el plan
        if not self.amount:
            self.amount = self.membership_plan.price
        super().save(*args, **kwargs)


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    entry_time = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['member', 'entry_time'],
                name='unique_attendance_per_day'
            )
        ]

    def __str__(self):
        return f"{self.member.user.email} - {self.entry_time}"

# class PhysicalEvaluation(models.Model):
#     evaluation_id = models.AutoField(primary_key=True)
#     member = models.ForeignKey(Member, on_delete=models.CASCADE)
#     evaluation_date = models.DateField()
#     weight = models.DecimalField(max_digits=5, decimal_places=2)
#     height = models.DecimalField(max_digits=5, decimal_places=2)
#     notes = models.TextField(blank=True)

#     def __str__(self):
#         return f"{self.member.user.email} - {self.evaluation_date}"
