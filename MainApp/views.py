from django.shortcuts import render
from django.views import View
from .models import Task


class BaseView(View):
    template_name = "MainApp/Base_form.html"

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, self.template_name, {"tasks": tasks})
