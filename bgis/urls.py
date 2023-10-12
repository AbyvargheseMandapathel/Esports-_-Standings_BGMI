from django.urls import path
from . import views

app_name = 'bgis'  # Optional, but useful for namespacing app URLs

urlpatterns = [
    path('', views.team_list, name='team_list'),
    # Add more URL patterns as needed
]
