from django.contrib import admin
from .models import Company, Task, SubTask, Comment

admin.site.register(Company)
admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Comment)
