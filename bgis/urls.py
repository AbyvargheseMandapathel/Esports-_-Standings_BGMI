from django.urls import path
from . import views

# urls.py in the 'bgis' app directory
app_name = 'bgis'

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('add_points/', views.add_points, name='add_points'),

    # Add more URL patterns as needed
]
