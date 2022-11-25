from django.shortcuts import render, redirect
from daylist.settings import BASE_DIR
from .models import Today_todo


def create(request):
    content = request.GET.get("context")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    Today_todo.objects.create(content=content, priority=priority, deadline=deadline)
    return redirect("todolist:read")


def read(request):
    todos_list = Today_todo.objects.all().order_by("id")
    return render(request, "todolist/view.html", {"context": todos_list})


def main(request):
    return render(request, "todolist/main.html")


def change(request, todo_pk):
    todo_list = Today_todo.objects.get(id=todo_pk)
    if todo_list.completed == True:
        todo_list.completed = False
    else:
        todo_list.completed = True
    todo_list.save()
    print(todo_list.completed)
    return redirect("todolist:read")


def delete(request, todo_pk):
    todo_list = Today_todo.objects.get(id=todo_pk)
    todo_list.delete()
    return redirect("todolist:read")
