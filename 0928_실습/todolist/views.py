from django.shortcuts import render
from .models import today_todo


def create(request):
    content = request.GET.get("title")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    today_todo.objects.create(content=content, priority=priority, deadline=deadline)

    context = {
        "context": content,
        "priority": priority,
        "deadline": deadline,
    }

    return render(request, "todolist/main.html", context)
