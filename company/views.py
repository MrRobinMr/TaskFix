from django.db.transaction import commit
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
import datetime
from .models import Company, Task, SubTask, Comment
from .forms import TaskForm, TaskEditForm, SubTaskForm
from django.contrib.auth.decorators import login_required

@login_required
def company_view(request, id):
    comapny = get_object_or_404(Company, pk=id)
    tasks = Task.objects.filter(company_id = id)
    return render(request, 'company.html', {'company':comapny, 'tasks': tasks})

@login_required
def task_new(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, company=company)
        if form.is_valid():
            task = form.save(commit=False)
            task.company = company
            task.save()
            form.save_m2m()
            return redirect('company', id=company_id)
    else:
        form = TaskForm(company=company)

    return render(request, 'task_new.html', {'form': form})

@login_required
def task_view(request, id):
    task = get_object_or_404(Task, pk=id)
    users = task.assigned_users.all()
    subtask = SubTask.objects.filter(task=id)
    return render(request, 'task_view.html', {'task': task, 'users':users, 'subtasks': subtask})

@login_required
def task_edit(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_view', id=id)
    else:
        form = TaskEditForm(instance=task)

    return render(request, 'task_edit.html', {'form': form, 'task': task})

@login_required
def subtask_new(request, task_id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = SubTaskForm(request.POST, task=task)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task
            subtask.start_date = datetime.date.today()
            subtask.save()
            subtask.save_m2m()
            return redirect('task_view', id=id)
    else:
        form = SubTaskForm(task=task)

    return render(request, 'subtask_new.html', {'form': form})