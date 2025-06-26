from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Task

# Create your views here.
def home(response):
    return HttpResponse("<h1>Kawinthida's Cyber Projects Portfolio</h1>")

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "cybr/list.html", {"name":ls.name})

def home(response):
	return render(response, "main/home.html", {"name": "test"})

# def index_nm(response, name):
#     ls = ToDoList.objects.get(name=name)
#     task = ls.task_set.all()
#     task_text = "<br>".join(task.text for task in task)

#     return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls.name, task_text))