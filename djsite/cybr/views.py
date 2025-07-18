from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Task
from .forms import CreateNewList

# Create your views here.
def home(response):
    return HttpResponse("<h1>Kawinthida's Cyber Projects Portfolio</h1>")

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "cybr/list.html", {"ls":ls})

def home(response):
	return render(response, "cybr/home.html", {"name": "test"})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()
    return render(response, "cybr/create.html", {"form":form})

# def index_nm(response, name):
#     ls = ToDoList.objects.get(name=name)
#     task = ls.task_set.all()
#     task_text = "<br>".join(task.text for task in task)

#     return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls.name, task_text))
