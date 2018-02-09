from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name = 'todo'

urlpatterns=[
    # Homepage
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    # About Page
    url(r'^about/$', views.AboutView.as_view(), name='about'),

    # Add Todo
    url(r'^todo/add_todo/$', views.AddTodo.as_view(), name='add_todo'),

    # Edit Todo
    url(r'^todo/(?P<pk>[0-9]+)/$', views.EditTodo.as_view(), name='edit_todo'),
    
    # Delete Todo
    url(r'^todo/(?P<pk>[0-9]+)/delete/$', views.DeleteTodo.as_view(), name='delete_todo'),

    # Landing Page
    url(r'^landing/$', views.LandingPage.as_view(), name='landing'),

    # Register Page
    url(r'^register/$', views.CreateUser.as_view(), name='register'),

    # Login
    url(r'^login/$', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),

    # Logout
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # Profile Page
    url(r'^account/$', views.ProfileView.as_view(), name='account'),


]