from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=64, blank=False, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='companies_owned')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='companies_created')
    start_date = models.DateField(blank=False)
    is_active = models.BooleanField(blank=False)
    logo = models.ImageField(upload_to='company_logo/', default='company_logo/default_company_logo.png')

    def __str__(self):
        return f"{self.name}"

class Task(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    describtion = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False, blank=False, related_name='task_company')
    assigned_users = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.title}"

class SubTask(models.Model):
    title =models.CharField(max_length=64, blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=True)
    assigned_users = models.ManyToManyField(User)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, blank=False, related_name='subtask_task')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='coment_user')
    content = models.TextField(blank=False, unique=False)
    date = models.DateField(blank=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False, blank=False, related_name='coment_task')

