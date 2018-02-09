from django.test import TestCase
from django.utils import timezone
from .models import Todo

# Tests for the app todo
class TodoEntryTest(TestCase):

    def test_string_representation(self):
        todo = Todo(
            todo_title = 'Buy tickets to pycon17',
            due_date = timezone.now(),
            priority = 'urgent',
            category = 'work'
        )
        self.assertEqual(str(todo), todo.todo_title)
    