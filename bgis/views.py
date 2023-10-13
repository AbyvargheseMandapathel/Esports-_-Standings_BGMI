from django.shortcuts import render, redirect
from .models import Points, Team
import logging
from django.db import transaction  # Import the transaction module
from .forms import PointsForm  # You should create a PointsForm for the input fields in your HTML form

def add_points(request):
    if request.method == 'POST':
        form = PointsForm(request.POST)
        if form.is_valid():
            team_name = form.cleaned_data['team_name']
            matches = form.cleaned_data['matches']
            win = form.cleaned_data['win']
            fp = form.cleaned_data['fp']
            pp = form.cleaned_data['pp']

            try:
                team = Team.objects.get(team_name=team_name)
                points, created = Points.objects.get_or_create(team=team, defaults={'matches': 0, 'win': 0, 'fp': 0, 'pp': 0})
                points.matches += matches
                points.win += win
                points.fp += fp
                points.pp += pp
                points.save()

                return redirect('bgis:team_list')  # Redirect to a success page after adding points
            except Team.DoesNotExist:
                return render(request, 'error_page.html', {'error_message': f"Team '{team_name}' does not exist."})

    else:
        form = PointsForm()  # Create an empty form for GET requests

    return render(request, 'add_points.html', {'form': form})



def team_list(request):
    teams = Points.objects.select_related('team').order_by('-tp', '-pp', 'fp', 'win')
    context = {'teams': teams}
    return render(request, 'result.html', context)
