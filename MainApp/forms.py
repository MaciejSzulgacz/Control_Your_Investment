from django import forms
from django.contrib.auth import get_user_model, authenticate

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
