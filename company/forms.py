from django import forms
from .models import Company, Task, SubTask, Comment


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']