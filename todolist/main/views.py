from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import Tables, Tasks


# Create your views here.

def filter_url(request, slug='all'):
    try:
        table = Tables.objects.get(slug=slug)
        category = table.category
        tasks = Tasks.objects.filter(category=table.id)
    except:
        tasks = Tasks.objects.all()
        category = 'All'

    context = {
        'tasks': tasks,
        'table_name': category
    }

    return render(request, 'show_tasks.html', context)


def task_menu(request, task_id):
    task = Tasks.objects.get(id=task_id)

    context = {
        'task_data': task
    }

    return render(request, 'task_data.html', context)


def remove_task(request, task_id):
    object = Tasks.objects.get(id=task_id).delete()

    return HttpResponseRedirect('/categories/all')


def edit(request, task_id):
    object = Tasks.objects.get(id=task_id)

    context = {
        'task_data': object
    }

    return render(request, 'edit.html', context)


def save(request, task_id):
    object = Tasks.objects.get(id=task_id)

    if request.method == 'POST':
        object.title = request.POST.get("title")
        object.discription = request.POST.get('discription')

        object.save()
        return HttpResponseRedirect('/categories/all')


def addTask(request):
    categories = Tables.objects.all()
    context = {
        "categories": categories
    }

    return render(request, 'addTask.html', context)


def saveTasks(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        discription = request.POST.get('description')
        data = request.POST.get('date')
        category = request.POST.get('category')
        print(category)

        table = Tables.objects.get(category=category)

        task = Tasks()
        task.title = title
        task.discription = discription
        task.data = data

        task.category_id = table.id

        if category:
            task.save()

            return HttpResponseRedirect('/categories/all')