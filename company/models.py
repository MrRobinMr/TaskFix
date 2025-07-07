from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=64, blank=False, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='companies_owned')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='companies_created')
    start_date = models.DateField(blank=False)
    is_active = models.BooleanField(blank=False)

    def __str__(self):
        return f"{self.name}"

class Task(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    describtion = models.TextField()