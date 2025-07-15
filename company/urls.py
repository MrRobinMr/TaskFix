from django.urls import path
from .views import company_view, task_new


urlpatterns = [
    path('<int:id>', company_view, name='company'),
    path('<int:company_id>/task/new/', task_new, name='task_new'),

]