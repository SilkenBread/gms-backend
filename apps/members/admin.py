from django.contrib import admin
from .models import Member, Payment, Attendance, PhysicalEvaluation


admin.site.register(Member)
admin.site.register(Payment)
admin.site.register(Attendance)
admin.site.register(PhysicalEvaluation)
