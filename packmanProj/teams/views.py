import uuid
from urllib import request

from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from subscribers.models import Subscriber
from .forms import TeamForm
from .models import Team


class TeamList(ListView):
    model = Team
    paginate_by = 5
    template_name = 'teams/team_list.html'
    context_object_name = 'teams'

    # protect the view so that only authenticated users can access it.
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TeamList, self).dispatch(*args, **kwargs)


@login_required()  # Decorating a FBV to ensures that only authenticated users can access this page.
def team_details(request, uuid):
    team = Team.objects.get(uuid=uuid)
    sub = get_object_or_404(Subscriber, user=request.user)
    variables = {
        'team': team,
        'sub': sub,
    }
    return render(request, 'teams/team_details.html', variables)


@login_required()
def team_create(request):
    print("in team_create")
    if request.POST:
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.owner = request.user
            team.save()
            sub = get_object_or_404(Subscriber, user=request.user)
            redirect_url = reverse('teams.views.team_details', args=(team.uuid,))  # reverse() can create the proper URL of a given view
            return HttpResponseRedirect(redirect_url)
    else:
        team = Team(owner=request.user)
        team.uuid = None;
        form = TeamForm()

    variables = {
        'form': form,
        'team': team
    }

    template = 'teams/team_create.html'
    return render(request, template, variables)


@login_required()
def team_update(request, uuid):
    print("in team_update", "uuid:", uuid)
    team = get_object_or_404(Team, uuid=uuid)
    if team.owner != request.user:
        print("team_update forbidden")
        # tried returning this: return HttpResponseForbidden() but i couldn;t get django to display 403.html. instead i render it directly -
        return render(request, '403.html')

    if request.POST:
        print("POST")
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            team = form.save(commit=False)
            team.owner = request.user
            team.save()
            redirect_url = reverse('teams.views.team_details', args=(team.uuid,))  # reverse() can create the proper URL of a given view
            return HttpResponseRedirect(redirect_url)
    else:
        form = TeamForm(instance=team)

    variables = {
        'form': form,
        'team': team
    }

    if request.is_ajax():  # will be true when called by the on_ready function in app.js
        template = 'teams/team_item_form.html'  # no need to refresh the entire page on edit team. only the team form should be returned.
    else:
        template = 'teams/team_create.html'
    return render(request, template, variables)


@login_required()
def team_join(request, uuid):
    team = Team.objects.get(uuid=uuid)
    sub = get_object_or_404(Subscriber, user=request.user)
    sub.team = team
    sub.save()
    variables = {
        'team': team,
        'sub': sub,
    }
    return render(request, 'teams/team_details.html', variables)


@login_required()
def team_leave(request, uuid):
    team = Team.objects.get(uuid=uuid)
    sub = get_object_or_404(Subscriber, user=request.user)
    sub.team = None
    sub.save()
    variables = {
        'team': team,
        'sub': sub,
    }
    return render(request, 'teams/team_details.html', variables)