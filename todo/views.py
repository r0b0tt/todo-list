from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

from datetime import date, timedelta

from .models import Todo
from .forms import TodoForm


class IndexView(View):
    """
    Index Page for the ToDo Web Application.
    """
    template_name = 'todo/todos.html'

    def get(self, request):
        # Delete Todos from previous days.
        passed_todos = Todo.objects.filter(due_date__lt=date.today())
        delete_previous_todos(passed_todos)

        # Get all Todos
        todos = Todo.objects.all().order_by('due_date')

        # Determine the dates for the next 7 days.
        todays_date = date.today()
        tomorrows_date = date.today() + timedelta(1)
        day3_date = date.today() + timedelta(2)
        day4_date = date.today() + timedelta(3)
        day5_date = date.today() + timedelta(4)
        day6_date = date.today() + timedelta(5)
        day7_date = date.today() + timedelta(6)

        # Store todos for different days in lists.
        todays_todos = []
        tomorrows_todos = []
        day3_todos = []
        day4_todos = []
        day5_todos = []
        day6_todos = []
        day7_todos = []

        for todo in todos:
            if todo.due_date == todays_date:
                todays_todos.append(todo)
            elif todo.due_date == tomorrows_date:
                tomorrows_todos.append(todo)
            elif todo.due_date == day3_date:
                day3_todos.append(todo)
            elif todo.due_date == day4_date:
                day4_todos.append(todo)
            elif todo.due_date == day5_date:
                day5_todos.append(todo)
            elif todo.due_date == day6_date:
                day6_todos.append(todo)
            elif todo.due_date == day7_date:
                day7_todos.append(todo)

        context = {
            'todos': todos,
            'todays_todos': todays_todos,
            'todays_date': todays_date,
            'tomorrows_todos': tomorrows_todos,
            'tomorrows_date': tomorrows_date,
            'day3_todos': day3_todos,
            'day3_date': day3_date,
            'day4_todos': day4_todos,
            'day4_date': day4_date,
            'day5_todos': day5_todos,
            'day5_date': day5_date,
            'day6_todos': day6_todos,
            'day6_date': day6_date,
            'day7_todos': day7_todos,
            'day7_date': day7_date,
        }
        return render(request, self.template_name, context)


class AboutView(View):
    """
    About page.
    """
    template_name = 'todo/about.html'

    def get(self, request):
        return render(request, self.template_name)


class AddTodo(CreateView):
    """
    Add a new todo.
    """
    model = Todo
    template_name = 'todo/todo.html'
    form_class = TodoForm
    success_url = '/'


class EditTodo(UpdateView):
    """
    Edit a todo.
    """
    model = Todo
    template_name = 'todo/todo.html'
    form_class = TodoForm
    success_url = '/'


class DeleteTodo(View):
    """
    Delete a todo.
    """

    def get(self, request, pk):
        Todo.objects.get(pk=pk).delete()
        return HttpResponseRedirect(reverse('todo:index'))


def delete_previous_todos(todos_list):
    """
    Delete todos from previous days
    """
    for todo in todos_list:
        todo.delete()
