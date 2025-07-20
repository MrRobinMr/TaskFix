from django import forms
from .models import Company, Task, SubTask, Comment, User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_users']
        widgets = {
            'assigned_users': forms.SelectMultiple(attrs={'class': 'form-select', 'id': 'id_assigned_users'}),
        }

    def __init__(self, *args, **kwargs):
        company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)
        if company:
            self.fields['assigned_users'].queryset = User.objects.filter(profile__company=company)
        else:
            self.fields['assigned_users'].queryset = User.objects.none()

class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']