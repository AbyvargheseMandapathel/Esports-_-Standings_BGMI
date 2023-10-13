from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/', null=True, blank=True)

    def __str__(self):
        return self.team_name

class Points(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    matches = models.IntegerField()
    win = models.IntegerField()
    fp = models.IntegerField()
    pp = models.IntegerField()
    tp = models.IntegerField()  # Add the 'tp' field here

    def __str__(self):
        return self.team.team_name  # Use the team's name as the string representation


    def save(self, *args, **kwargs):
        # Calculate TP as the sum of FP and PP before saving
        self.tp = self.fp + self.pp
        super(Points, self).save(*args, **kwargs)
