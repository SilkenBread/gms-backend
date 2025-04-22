from django.contrib import admin

from .models import Attendance, Member, Payment, PhysicalEvaluation

admin.site.register(Member)
admin.site.register(Payment)
admin.site.register(Attendance)
admin.site.register(PhysicalEvaluation)
