from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import Company

def company_view(request, id):
    comapny = get_object_or_404(Company, pk=id)
    return render(request, 'company.html', {'company':comapny})

