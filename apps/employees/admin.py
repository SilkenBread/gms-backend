from django.contrib import admin

from .models import Employee, Equipment, Maintenance

admin.site.register(Equipment)
admin.site.register(Maintenance)
admin.site.register(Employee)
