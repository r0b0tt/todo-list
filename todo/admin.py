from django.contrib import admin

# Import our models
from .models import Todo

admin.site.register(Todo)
