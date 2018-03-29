from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User

from .models import Todo


class TodoForm(forms.ModelForm):
    todo_title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Todo'}))
    due_date = forms.DateField(label='Due Date', widget=AdminDateWidget)
    category = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Category eg: family'}))

    class Meta:
        model = Todo
        fields = ['todo_title', 'due_date', 'priority', 'category']
