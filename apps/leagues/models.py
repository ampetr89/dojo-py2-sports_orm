from django.db import models
from django.forms.models import model_to_dict

class League(models.Model):
    name = models.CharField(max_length=50)
    sport = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def as_dict(self):
        d1 = model_to_dict(self)
        teams = self.team_set.all()
        d1.update({'teams': [team.as_dict() for team in teams]})
        return d1

class Team(models.Model):
    location = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50)
    league = models.ForeignKey(League)

    def __str__(self):
        return self.location+' '+self.team_name

    def as_dict(self):
        d1 = model_to_dict(self)
        players = self.player_set.all()
        d1.update({'players': [player.as_dict() for player in players]})
        return d1

class Player(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    curr_team = models.ForeignKey(Team) # , related_name="curr_players"
    # all_teams = models.ManyToManyField(Team, related_name="all_players")

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def as_dict(self):
        d1 = model_to_dict(self)
    
        return d1