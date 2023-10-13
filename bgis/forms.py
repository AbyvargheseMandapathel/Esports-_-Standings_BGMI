from django import forms
from .models import Team, Points

class PointsForm(forms.Form):
    team_name = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        label='Team Name',
        empty_label='Select a Team'
    )
    matches = forms.IntegerField(label='Matches')
    win = forms.IntegerField(label='Wins')
    fp = forms.IntegerField(label='FP')
    pp = forms.IntegerField(label='PP')

    def clean_team_name(self):
        team_name = self.cleaned_data['team_name']
        # No need to check if the team exists because ModelChoiceField handles this validation
        return team_name
