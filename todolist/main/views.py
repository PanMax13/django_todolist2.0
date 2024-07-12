from django.shortcuts import render, HttpResponse
from .models import Tables, Tasks
# Create your views here.

def all(request):
    tables = Tables.objects.all()

    return render(request, 'base.html')

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