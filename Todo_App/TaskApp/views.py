from django.shortcuts import render, redirect,reverse
from TaskApp.models import TaskDetails
from .forms import TaskForm
from django.http import HttpResponseRedirect

import datetime
# Create your views here.
def view_task_details(request):
    data = TaskDetails.objects.all()
    return render(request, "task_details.html", {"data":data})

def view_home(request):
    return render(request, "home.html")


def view_register(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = TaskDetails()
            obj.title = form.cleaned_data['title']
            obj.description = form.cleaned_data['description']
            obj.status = form.cleaned_data['status']

            obj.save()
        else:
            raise form.ValidationErrors
        return HttpResponseRedirect(reverse(view_task_details))
    else:
        form = TaskForm()

    return render(request, 'addtask.html', {'form': form})



def view_delete(request, pid):
    task = TaskDetails.objects.get(id = pid)
    task.delete()
    return redirect(view_task_details)

def view_update(request, pid):
    task = TaskDetails.objects.get(id = pid)
    if request.method == "post":
        data = request.POST
        task.title = data.get("title")
        task.description = data.get("description")
        task.status = data.get("status")

        task.save()
        return redirect(view_task_details)
    return render(request, "update.html", {'data':task})