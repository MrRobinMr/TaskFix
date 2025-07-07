from django.urls import path
from .views import company_view


urlpatterns = [
    path('<int:id>', company_view, name='company'),

]