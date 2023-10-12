from django.shortcuts import render
from .models import Team

def team_list(request):
    teams = Team.objects.all().order_by('-tp', '-pp', 'fp')
    # '-tp' sorts in descending order of TP, '-pp' in descending order of PP, 'fp' in ascending order of FP
    
    context = {'teams': teams}
    
    return render(request, 'result.html', context)
