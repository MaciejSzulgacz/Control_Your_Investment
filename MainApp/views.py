# from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from .models import Machine, Task
from django.views.generic import CreateView, UpdateView
from django.forms.widgets import SelectDateWidget


class BaseView(View):
    template_name = "MainApp/Base_form.html"

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, self.template_name, {"tasks": tasks})


class TaskCreateView(CreateView):
    model = Task
    fields = ['name', 'start_date', 'finish_date', 'person']
    success_url = reverse_lazy('add-task')

    def get_form(self):
        form = super(TaskCreateView, self).get_form()
        form.fields['start_date'].widget = SelectDateWidget()
        form.fields['finish_date'].widget = SelectDateWidget()
        return form


class DeleteTaskView(View):

    def get(self, request, my_id, *args, **kwargs):
        task = Task.objects.get(id=my_id)
        task.delete()
        return redirect("/")


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['name', 'start_date', 'finish_date', 'person', 'machine']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('base')


class MachineCreateView(CreateView):
    model = Machine
    fields = ['machine_model', 'description']
    success_url = reverse_lazy('add-machine')
