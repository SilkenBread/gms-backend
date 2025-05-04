from django.contrib import admin

from .models import Attendance, Member

admin.site.register(Member)
admin.site.register(Attendance)
# admin.site.register(Payment)
# admin.site.register(PhysicalEvaluation)
