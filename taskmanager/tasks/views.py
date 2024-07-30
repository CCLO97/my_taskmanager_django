from django.shortcuts import render, redirect

# Create your views here.
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
def task_create(request):
    if request.methhod == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form - TaskForm()
    return render(request, 'tasks/task_form.html', {'form' : form})