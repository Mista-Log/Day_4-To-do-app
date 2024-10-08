from django.shortcuts import render, redirect, get_object_or_404
from .models import List




# Create your views here.
def index(request):
    tasks = List.objects.all()

    if request.method == "POST":
        task = request.POST.get('task')
        lists = List(task=task)
        if task:
            lists.save()
            return redirect('index')
    
    context = {'tasks': tasks}
    return render(request, 'index.html', context)

def update(request, pk):
    task = List.objects.get(id=pk)
    if request.method == 'POST':
        update_task = request.POST.get('update')
        if update_task:
            task.task = update_task
            task.save()
            return redirect('index')
    context = {'task': task}
    return render(request, 'update.html', context)

def delete(request, pk):
    task = List.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('index')

    context = {'task': task}
    return render(request, 'delete.html', context)