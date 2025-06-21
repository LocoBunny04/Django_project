from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Task

# Create your views here.
def home(response):
    return HttpResponse("<h1>Kawinthida's Cyber Projects Portfolio</h1>")

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" % ls.name)

# def index_nm(response, name):
#     ls = ToDoList.objects.get(name=name)
#     item = ls.item_set.all()
#     items_text = "<br>".join(item.text for item in item)

#     return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" % (ls.name, items_text))