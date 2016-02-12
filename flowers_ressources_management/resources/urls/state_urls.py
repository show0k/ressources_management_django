from django.conf.urls import patterns, url
from ..views import (StateListView, StateCreateView, StateDetailView,
                     StateUpdateView, StateDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(StateCreateView.as_view()),
        name="state_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(StateUpdateView.as_view()),
        name="state_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(StateDeleteView.as_view()),
        name="state_delete"),

    url(r'^(?P<pk>\d+)/$',
        StateDetailView.as_view(),
        name="state_detail"),

    url(r'^$',
        StateListView.as_view(),
        name="state_list"),
)
