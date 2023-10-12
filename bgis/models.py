from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    matches = models.IntegerField()
    win = models.IntegerField()
    fp = models.IntegerField()
    pp = models.IntegerField()
    tp = models.IntegerField()

    def __str__(self):
        return self.team_name

    def save(self, *args, **kwargs):
        # Calculate TP as the sum of FP and PP before saving
        self.tp = self.fp + self.pp
        super(Team, self).save(*args, **kwargs)
