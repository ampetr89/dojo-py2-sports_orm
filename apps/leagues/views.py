from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.http import JsonResponse
from .models import League, Team, Player

from . import team_maker

def index(request):
    return render(request, "leagues/index.html")

def make_data(request):
    team_maker.gen_leagues(10)
    team_maker.gen_teams(50)
    team_maker.gen_players(200)

    return redirect("index")

def get_results(request):
    if request.method=='GET':
        return redirect('/')
    num = request.POST['question']
    
    print('num')
    print(num)

    num = int(num)
    if num == 0:
        players = Player.objects.all()
    elif num == 1:
        # 1 all baseball leagues
        players = Player.objects.filter(curr_team__league__sport='Baseball')
        
    elif num == 2:
        # 2 all womens' leagues
        players = Player.objects.filter(curr_team__league__name__contains='Women')
        
    elif num == 3:
        # 3 all leagues where sport is any type of hockey
        players = Player.objects.filter(curr_team__league__sport__contains='Hockey')
        
    elif num == 4:
        # 4 all leagues where sport is something OTHER THAN football
        players = Player.objects.exclude(curr_team__league__sport='Football')
        
    elif num == 5:
        # 5 all leagues that call themselves "conferences"
        players = Player.objects.filter(curr_team__league__name__contains='Conference')
        
    elif num == 6:
        # 6 all leagues in the Atlantic region
        players = Player.objects.filter(curr_team__league__name__contains='Atlantic')
        
    elif num == 7:
        # 7 all teams based in Dallas
        players = Player.objects.filter(curr_team__location='Dallas')
        
    elif num == 8:
        # 8 all teams named the Raptors
        players = Player.objects.filter(curr_team__name='Raptors')
    
    elif num == 9:
        # 9 all teams whose location includes "City"
        players = Player.objects.filter(curr_team__location__contains='City')

    elif num == 10:
        #10 all teams whose names begin with "T"
        players = Player.objects.filter(curr_team__team_name__startswith='T')
    
    elif num in [11, 12]:
        #11 all teams, ordered alphabetically by location
        #12 all teams, ordered by team name in reverse alphabetical order
        players = Player.objects.exclude()
        # .... idk how to sort a dictionary.... 

    elif num == 13:
        #13 every player with last name "Cooper"
        players = Player.objects.filter(last_name='Cooper')

    elif num == 14:
        #14 every player with first name "Joshua"
        players = Player.objects.filter(first_name='Joshua')

    elif num == 15:
        #15 every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
        players = Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua')

    elif num == 16:
        #16 all players with first name "Alexander" OR first name "Wyatt"
        players = Player.objects.filter(first_name='Alexander')|filter(first_name='Wyatt')

    leagues = {}
    for player in players:
        team = player.curr_team
        league = team.league
        if league.id not in leagues:
            leagues.update({league.id: model_to_dict(league)})
            leagues[league.id].update({'teams': {} })

        # all_league_teams = team.league.team_set.all()
        if team.id not in leagues[league.id]['teams']:
            leagues[league.id]['teams'].update({team.id: model_to_dict(team)})
            leagues[league.id]['teams'][team.id].update({'players': {}})

        leagues[league.id]['teams'][team.id]['players'].update({player.id: model_to_dict(player)})


    # print(context)
    context = {
        'leagues': leagues
    }

    return JsonResponse(context)
