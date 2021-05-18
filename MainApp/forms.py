from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

from .models import *

User = get_user_model()


class LoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password']

    def clean(self):
        cd = super().clean()
        username = cd['username']
        password = cd['password']
        user = authenticate(username=username, password=password)
        if user is None:
            self.add_error(None, 'Podaj poprawne dane!')


def validate_date(start_date, finish_date):
    if finish_date < start_date:
        raise ValidationError("Start date should be earlier than finish date.")


class TaskForm(forms.Form):
    name = models.CharField(max_length=128)
    start_date = models.DateField()
    finish_date = models.DateField(validators=[validate_date], null=True, default=None)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    machine = models.ManyToManyField(Machine, related_name='machine')

    # class Meta:
    #     model = Task
    #     fields = ['name', 'start_date', 'finish_date', 'person', 'machine']



