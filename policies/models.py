from django.db import models
from django.core.validators import MinValueValidator
from datetime import date

class Policy(models.Model):
    POLICY_TYPES = [
        ('auto', 'Auto'),
        ('home', 'Home'),
        ('life', 'Life'),
        ('health', 'Health'),
    ]

    policy_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    policy_type = models.CharField(max_length=20, choices=POLICY_TYPES)
    expiry_date = models.DateField(validators=[MinValueValidator(date.today())])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.policy_type} ({self.policy_id})"

    class Meta:
        verbose_name_plural = "Policies"
