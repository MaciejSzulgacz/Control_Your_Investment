from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from .models import Machine, Person, Task, Image
from django.views.generic import CreateView, FormView, UpdateView, RedirectView
from django.forms.widgets import SelectDateWidget
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm, TaskForm


class BaseView(View):
    template_name = "MainApp/Base_form.html"

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        persons = Person.objects.all()
        machines = Machine.objects.all()
        return render(request, self.template_name, {"tasks": tasks, "persons": persons, "machines": machines})


class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Task
    fields = ['name', 'start_date', 'finish_date', 'person']
    success_url = reverse_lazy('add-task')

    def get_form(self):
        form = super(TaskCreateView, self).get_form()
        form.fields['start_date'].widget = SelectDateWidget()
        form.fields['finish_date'].widget = SelectDateWidget()
        return form

# class TaskCreateView(View):
#     template_name = 'MainApp/task_form2.html'
#     form_class = TaskForm
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {"form": form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         return render(request, self.template_name, {"form": form})


class TaskDeleteView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, my_id, *args, **kwargs):
        task = Task.objects.get(id=my_id)
        task.delete()
        return redirect("/")


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Task
    fields = ['name', 'start_date', 'finish_date', 'person', 'machine', 'done']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('base')


class MachineCreateView(CreateView):
    model = Machine
    fields = ['machine_model', 'description']
    success_url = reverse_lazy('add-machine')


class MachineDeleteView(View):
    def get(self, request, my_id, *args, **kwargs):
        machine = Machine.objects.get(id=my_id)
        machine.delete()
        return redirect("/")


class MachineUpdateView(UpdateView):
    model = Machine
    fields = ['machine_model', 'description']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('base')


class PersonCreateView(CreateView):
    model = Person
    fields = ['full_name', 'position']
    success_url = reverse_lazy('add-person')


class PersonDeleteView(View):
    def get(self, request, my_id, *args, **kwargs):
        person = Person.objects.get(id=my_id)
        person.delete()
        return redirect("/")


class PersonUpdateView(UpdateView):
    model = Person
    fields = ['full_name', 'position']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('base')


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


class LogoutView(RedirectView):
    url = reverse_lazy('base')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request)


class ImageCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Image
    fields = ['task', 'image']
    success_url = reverse_lazy('add-image')


class DetailsTaskView(View):
    template_name = 'MainApp/details_task.html'

    def get(self, request, my_id, *args, **kwargs):
        task = Task.objects.get(id=my_id)
        return render(request, self.template_name, {"task": task})

# class ImageCreateView(LoginRequiredMixin, CreateView):
#     template_name = 'MainApp/image_form.html'
#     login_url = '/login/'
#     success_url = reverse_lazy('add-image')
#
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name)
#
#     def post(self, request, *args, **kwargs):
#         name = request.POST.get('name')
#         task = request.POST.get('task')
#         image = request.POST.get('image')
#         tasks = Task.objects.get(name=task)
#         if not name:
#             message = "Enter the name."
#             return render(request, self.template_name, {'message': message})
#         if Image.objects.filter(name=name):
#             message = "Name is already used."
#             return render(request, self.template_name, {'message': message})
#         if all([name, task, image]):
#             Image.objects.create(name=name, task=tasks, image=image)
#         return render(request, self.template_name, {"tasks": tasks})


class PersonListView(View):
    template_name = "MainApp/Person_list.html"

    def get(self, request, *args, **kwargs):
        persons = Person.objects.all()
        return render(request, self.template_name, {"persons": persons})


class MachineListView(View):
    template_name = "MainApp/Machine_list.html"

    def get(self, request, *args, **kwargs):
        machines = Machine.objects.all()
        return render(request, self.template_name, {"machines": machines})
