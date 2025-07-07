from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from company.models import Company
from users.models import User


@login_required
def home_view(request):
    companys = Company.objects.all()
    return render(request, 'home.html', {"companys" : companys})

