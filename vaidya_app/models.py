from django.db import models
from django.contrib.auth.hashers import make_password

class SignupCDA(models.Model):
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Hash only if password is not already hashed
        if not self.password.startswith("pbkdf2_sha256$"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.email})"

class SignupDOCTORS(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    specialisation = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    ngo = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Hash only if password is not already hashed
        if not self.password.startswith("pbkdf2_sha256$"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.email})"
    
class SignupNGO(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.EmailField(unique=True)
    website = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Hash only if password is not already hashed
        if not self.password.startswith("pbkdf2_sha256$"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.email})"

class ConsultationBooking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    doctor = models.CharField(max_length=100)
    reason = models.TextField()
    diagnosis_report = models.FileField(upload_to="diagnosis_reports/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # doctor = models.ForeignKey(SignupDOCTORS, on_delete=models.CASCADE, related_name="appointments", null=True, blank=True)
    # patient = models.ForeignKey(SignupCDA, on_delete=models.CASCADE, related_name="appointments", null=True, blank=True)
    schedule_date = models.DateTimeField(blank=True, null=True)
    gmeet_link = models.URLField(blank=True, null=True)
    def __str__(self):
        return f"{self.name} - {self.doctor}"
    
class HealthReport(models.Model):
    REPORT_CHOICES = [
        ('Illness', 'Illness'),
        ('Outbreak', 'Outbreak'),
        ('Mental Health Crisis', 'Mental Health Crisis'),
    ]

    report_type = models.CharField(max_length=50, choices=REPORT_CHOICES)
    location = models.CharField(max_length=255)
    details = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_type} at {self.location} ({self.submitted_at.strftime('%Y-%m-%d %H:%M')})"
    
class Campaign(models.Model):
    CAMPAIGN_TYPES = [
        ('health', 'Health Camp'),
        ('education', 'Education Drive'),
        ('environment', 'Environment Awareness'),
        ('charity', 'Charity Event'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=CAMPAIGN_TYPES)

    def __str__(self):
        return self.title


class Admin(models.Model):
    full_name = models.CharField(max_length=100)
    # address = models.EmailField(unique=True)
    # website = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Hash only if password is not already hashed
        if not self.password.startswith("pbkdf2_sha256$"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.email})"