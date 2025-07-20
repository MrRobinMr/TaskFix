from django.urls import path
from .views import company_view, task_new, task_view, task_edit


urlpatterns = [
    path('<int:id>', company_view, name='company'),
    path('<int:company_id>/task/new/', task_new, name='task_new'),
    path('task/<int:id>', task_view, name='task_view'),
    path('task/edit/<int:id>', task_edit, name='task_edit'),

]