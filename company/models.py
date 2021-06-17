from django.db import models

# Create your models here.
from user.models import Employee


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18)
    trading_name = models.CharField(max_length=200, blank=True, null=True)
    employees = models.ManyToManyField(Employee, blank=True)

    class Meta:
        db_table = "company"
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
