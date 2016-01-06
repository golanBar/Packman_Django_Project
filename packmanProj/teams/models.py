import uuid
from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=80)
    owner = models.ForeignKey(User)  # only the owner will be able to delete the team.
    created_on = models.DateField(auto_now_add=True)
    desc = models.CharField(default="", max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'teams'

    def __unicode__(self):
        return u"%s" % self.name

    @models.permalink
    def get_absolute_url(self):
        return 'team_det', [self.uuid]

    @models.permalink
    def get_update_url(self):
        return 'team_upd', [self.uuid]

    @models.permalink
    def get_delete_url(self):
        return 'team_delete', [self.uuid]

    @models.permalink
    def get_join_url(self):
        return 'team_joi', [self.uuid]

    @models.permalink
    def get_leave_url(self):
        return 'team_lea', [self.uuid]
