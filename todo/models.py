from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    """ Database model for todo app """
    PRIORITY_CHOICES = (
        ('urgent', 'urgent'),
        ('not urgent', 'not urgent'),
    )
    todo_title = models.CharField(max_length=300, blank=False, null=False)
    due_date = models.DateField(blank=False)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, blank=False)
    category = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.todo_title
