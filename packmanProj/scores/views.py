from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Avg, Max, Sum
from django.views.decorators.csrf import csrf_exempt

from subscribers.models import Subscriber
from teams.models import Team


@login_required()
def scores_details(request):
    sub = Subscriber.objects.get(user=request.user)
    # traverse the Team<->Subscriber foreign key relationship backwards.
    teams_avg = Team.objects.annotate(avg_score_for_all_users_in_team=Avg('subscriber__avg_score')).order_by('-avg_score_for_all_users_in_team')
    best_team = teams_avg[0]
    best_team_num_games = Subscriber.objects.filter(team=best_team).aggregate(num_games_alias=Sum('num_games'))
    best_team_best_score = Subscriber.objects.filter(team=best_team).aggregate(best_score_alias=Max('best_score'))
    best_team_dict = {"name": best_team.name,
                      "num_games": best_team_num_games['num_games_alias'],
                      "avg_score": best_team.avg_score_for_all_users_in_team,
                      "best_score": best_team_best_score['best_score_alias']}
    variables = {
        'sub': sub,
        'best_team': best_team_dict
    }
    return render(request, 'scores/scores_details.html', variables)


@csrf_exempt
def persist_score(request):
    print("in persist_score")
    body_Unicode = request.body.decode(encoding='UTF-8')
    new_score = int(body_Unicode.split('&')[0].split('score=')[1])
    username = body_Unicode.split('&')[1].split('username=')[1]

    # update user's data
    sub = Subscriber.objects.get(user__username=username)
    if sub is not None:
        if sub.best_score < new_score:
            sub.best_score = new_score
        sub.avg_score = ((sub.avg_score*sub.num_games) + new_score)/(sub.num_games+1)
        sub.num_games += 1
        sub.save()

    return(None)