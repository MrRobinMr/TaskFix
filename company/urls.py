from django.urls import path
from .views import company_view, task_new


urlpatterns = [
    path('<int:id>', company_view, name='company'),
    path('task/New', task_new, name='task_new'),

]