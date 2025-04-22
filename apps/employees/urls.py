from rest_framework.routers import DefaultRouter

from .views import EmployeeViewSet, EquipmentViewSet, MaintenanceViewSet

router = DefaultRouter()
router.register("employees", EmployeeViewSet, basename="employees")
router.register("equipment", EquipmentViewSet, basename="equipment")
router.register("maintenance", MaintenanceViewSet, basename="maintenance")

urlpatterns = router.urls
