from django.db import models

class Car(models.Model):
    type = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    year = models.IntegerField()
    vin_number = models.CharField(max_length=100, unique=True)
    engine_number = models.CharField(max_length=100, unique=True)
    horsepower = models.IntegerField()
    state_number = models.CharField(max_length=50, unique=True)
    tech_passport_number = models.CharField(max_length=100, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.tech_passport_number:
            self.tech_passport_number = self.generate_tech_passport_number()
        super().save(*args, **kwargs)

    def generate_tech_passport_number(self):
        import uuid
        return str(uuid.uuid4())

    def __str__(self):
        return f"{self.type} {self.model} ({self.state_number})"

class DriverLicense(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField()
    category = models.CharField(max_length=10)
    issued_by = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.license_number:
            self.license_number = self.generate_license_number()
        super().save(*args, **kwargs)

    def generate_license_number(self):
        import uuid
        return str(uuid.uuid4())

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.license_number})"
