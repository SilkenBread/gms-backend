from rest_framework.routers import DefaultRouter

from .views import ScheduleViewSet, ServiceViewSet

router = DefaultRouter()
router.register("services", ServiceViewSet, basename="service")
router.register("schedules", ScheduleViewSet, basename="schedule")

urlpatterns = router.urls
