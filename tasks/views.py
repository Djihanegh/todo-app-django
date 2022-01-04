from django.shortcuts import render

from tasks.models import Task


def index(request):
    tasks = Task.objects.all()

    context = {'tasks': tasks}

    return render(
        request, 'tasks/list.html', context
    )
