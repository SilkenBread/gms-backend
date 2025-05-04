from rest_framework.routers import DefaultRouter

from .views import MemberViewSet, AttendanceViewSet

router = DefaultRouter()
router.register("members", MemberViewSet, basename="member")
router.register("attendance", AttendanceViewSet, basename="attendance")

urlpatterns = router.urls
