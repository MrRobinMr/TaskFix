from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import Company, Task, SubTask, Comment
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

def company_view(request, id):
    comapny = get_object_or_404(Company, pk=id)
    tasks = Task.objects.filter(company_id = id)
    return render(request, 'company.html', {'company':comapny, 'tasks': tasks})

@login_required
def task_new(request):
    task_form = TaskForm(request.POST or None, request.FILES or None)

    if task_form.is_valid():
        task = task_form.save(commit=False)
        task.save()
        return redirect(company_view)

    return render(request, 'task_edit.html', {'form': task_form, 'new': True})