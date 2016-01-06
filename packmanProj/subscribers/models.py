from django.db import models
from django.contrib.auth.models import User

from teams.models import Team


class Subscriber(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=2, blank=True)
    age = models.CharField(max_length=2, blank=True)
    best_score = models.IntegerField(default=0)
    avg_score = models.IntegerField(default=0)
    num_games = models.IntegerField(default=0)
    team = models.ForeignKey(Team, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'subscribers'

    def __unicode__(self):
        return u"%s's Subscription Info" % self.user_rec
