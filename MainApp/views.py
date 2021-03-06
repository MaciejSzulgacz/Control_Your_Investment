from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.widgets import SelectDateWidget
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView, UpdateView, RedirectView
from .forms import LoginForm
from .models import Machine, Person, Task, Image


# View of tasks
class BaseView(View):
    template_name = "MainApp/Base_form.html"

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        persons = Person.objects.all()
        machines = Machine.objects.all()
        return render(request, self.template_name, {"tasks": tasks, "persons": persons, "machines": machines})


# Task creating
class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Task
    fields = ['name', 'start_date', 'finish_date', 'person', 'machine', 'done']
    success_url = reverse_lazy('add-task')

    def get_form(self):
        form = super(TaskCreateView, self).get_form()
        form.fields['start_date'].widget = SelectDateWidget()
        form.fields['finish_date'].widget = SelectDateWidget()
        form.fields['finish_date'].required = False
        form.fields['machine'].required = False
        return form


# Task deleting
class TaskDeleteView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, my_id, *args, **kwargs):
        task = Task.objects.get(id=my_id)
        task.delete()
        return redirect("/")


# Task updating
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Task
    fields = ['name', 'start_date', 'finish_date', 'person', 'machine', 'done']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('base')

    def get_form(self):
        form = super(TaskUpdateView, self).get_form()
        form.fields['start_date'].widget = SelectDateWidget()
        form.fields['finish_date'].widget = SelectDateWidget()
        form.fields['finish_date'].required = False
        form.fields['machine'].required = False
        return form


# Machine creating
class MachineCreateView(CreateView):
    model = Machine
    fields = ['machine_model', 'description']
    success_url = reverse_lazy('add-machine')


# Machine deleting
class MachineDeleteView(View):
    def get(self, request, my_id, *args, **kwargs):
        machine = Machine.objects.get(id=my_id)
        machine.delete()
        return redirect("/machine-list/")


# Machine updating
class MachineUpdateView(UpdateView):
    model = Machine
    fields = ['machine_model', 'description']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('base')


# Person creating
class PersonCreateView(CreateView):
    model = Person
    fields = ['full_name', 'position']
    success_url = reverse_lazy('add-person')


# Person deleting
class PersonDeleteView(View):
    def get(self, request, my_id, *args, **kwargs):
        person = Person.objects.get(id=my_id)
        person.delete()
        return redirect("/person-list/")


# Person updating
class PersonUpdateView(UpdateView):
    model = Person
    fields = ['full_name', 'position']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('base')


# Login
class LoginView(FormView):
    form_class = LoginForm
    template_name = "MainApp/login.html"
    success_url = reverse_lazy('base')

    def form_valid(self, form):
        cd = form.cleaned_data
        username = cd['username']
        password = cd['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)


# Logout
class LogoutView(RedirectView):
    url = reverse_lazy('base')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request)


# Image adding
class ImageCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Image
    fields = ['task', 'upload']
    success_url = reverse_lazy('add-image')


# Details of tasks
class DetailsTaskView(View):
    template_name = 'MainApp/details_task.html'

    def get(self, request, my_id, *args, **kwargs):
        task = Task.objects.get(id=my_id)
        return render(request, self.template_name, {"task": task})


# List of persons
class PersonListView(View):
    template_name = "MainApp/Person_list.html"

    def get(self, request, *args, **kwargs):
        persons = Person.objects.all()
        return render(request, self.template_name, {"persons": persons})


# List of machines
class MachineListView(View):
    template_name = "MainApp/Machine_list.html"

    def get(self, request, *args, **kwargs):
        machines = Machine.objects.all()
        return render(request, self.template_name, {"machines": machines})
