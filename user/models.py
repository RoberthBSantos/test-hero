from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Employee(models.Model):
    user_django = models.OneToOneField(User, related_name='employed', on_delete=models.CASCADE, unique=True)
    cpf = models.CharField(max_length=18, blank=True)

    class Meta:
        db_table = "employee"
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
