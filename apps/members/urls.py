from rest_framework.routers import DefaultRouter

from .views import MemberViewSet, AttendanceViewSet, MembershipPlanViewSet, PaymentViewSet

router = DefaultRouter()
router.register("members", MemberViewSet, basename="member")
router.register("attendance", AttendanceViewSet, basename="attendance")
router.register(r'membership-plans', MembershipPlanViewSet, basename='membership-plan')
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = router.urls
