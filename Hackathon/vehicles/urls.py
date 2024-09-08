from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, DriverLicenseViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'driverlicenses', DriverLicenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
