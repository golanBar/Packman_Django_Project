"""packmanProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from greetings.views import HomePage
from django.contrib import admin

from teams.views import TeamList

urlpatterns = patterns(
        '',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^$', HomePage.as_view(), name="home"),  # using a class based view
        url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
        url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),
        url(r'^signup/$', 'subscribers.views.subscriber_new', name='sub_new'),  # using a function based view
        url(r'^subscriber/$', 'subscribers.views.subscriber_details', name='sub_det'),  # using a function based view
        url(r'^team/list/$', TeamList.as_view(), name='team_list'),  # CBV
        url(r'^team/new/$', 'teams.views.team_create', name='team_cre'),
        url(r'^team/(?P<uuid>[\w-]+)/$', 'teams.views.team_details', name='team_det'),
        url(r'^team/(?P<uuid>[\w-]+)/edit/$', 'teams.views.team_update', name='team_upd'),
        url(r'^team/(?P<uuid>[\w-]+)/join/$', 'teams.views.team_join', name='team_joi'),
        url(r'^team/(?P<uuid>[\w-]+)/leave/$', 'teams.views.team_leave', name='team_lea'),
        url(r'^scores/$', 'scores.views.scores_details', name='scores_det'),
        url(r'^persistScore/$', 'scores.views.persist_score', name='scores_per')
)
