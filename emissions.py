from django.db import models
from companies.models import Company
from ingestion.models import RawRecord


class NormalizedEmissionRecord(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
        ('LOCKED', 'LOCKED'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    scope = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    activity_value = models.FloatField()
    normalized_unit = models.CharField(max_length=50)

    emissions_kg_co2e = models.FloatField()

    suspicious_flag = models.BooleanField(default=False)

    approval_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    raw_record = models.ForeignKey(RawRecord, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
