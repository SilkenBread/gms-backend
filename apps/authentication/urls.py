from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import AuthenticationViewSet

router = DefaultRouter()
router.register("auth", AuthenticationViewSet, basename="auth")

urlpatterns = router.urls + [
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
