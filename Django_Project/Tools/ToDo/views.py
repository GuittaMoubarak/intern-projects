from django.shortcuts import render, redirect
from .forms import newTask
from .models import Task
from datetime import datetime
# Create your views here.


def index(request):
    tasks = Task.objects.all().filter(addDate=datetime.today())
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = newTask(request.POST)
        # check whether it's valid:
        if form.is_valid():
            body = form.cleaned_data["body"]
            task = Task(title=body)
            task.save()
            # return redirect("/ToDo/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = newTask()

    return render(request, "ToDo/index.html", {'form': form, 'tasks': tasks})


def check(request, id):
    task = Task.objects.get(id=id)
    if task.checked == True:
        task.checked = False
    else:
        task.checked = True
    task.save()
    return redirect(request.META.get('HTTP_REFERER'))

def remove(request, id):
    task= Task.objects.get(id=id)
    task.delete()
    return redirect(request.META.get('HTTP_REFERER'))