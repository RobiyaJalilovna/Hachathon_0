from rest_framework import viewsets
from .models import Car, DriverLicense
from .serializers import CarSerializer, DriverLicenseSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class DriverLicenseViewSet(viewsets.ModelViewSet):
    queryset = DriverLicense.objects.all()
    serializer_class = DriverLicenseSerializer
