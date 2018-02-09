from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User

from .models import Todo

class TodoForm(forms.ModelForm):
    todo_title = forms.CharField(label = '', widget=forms.TextInput(attrs={'placeholder':'Enter Todo'}))
    due_date = forms.DateField(label='Due Date', widget=AdminDateWidget)
    category = forms.CharField(label = '', widget=forms.TextInput(attrs={'placeholder':'Category eg: family'}))

    class Meta:
        model = Todo
        fields = ['todo_title', 'due_date', 'priority', 'category']

class UserForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder':'Email Address'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']

