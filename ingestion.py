from django.contrib.auth.models import User


class DataSource(models.Model):
    SOURCE_CHOICES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'UTILITY'),
        ('TRAVEL', 'TRAVEL'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    source_type = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f"{self.company.name} - {self.source_type}"
class RawRecord(models.Model):
    datasource = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    raw_payload = models.JSONField()
    ingest_status = models.CharField(max_length=50, default='PENDING')
    validation_errors = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)