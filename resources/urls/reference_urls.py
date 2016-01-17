from django.conf.urls import patterns, url
from ..views import (ReferenceListView, ReferenceCreateView, ReferenceDetailView,
                     ReferenceUpdateView, ReferenceDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(ReferenceCreateView.as_view()),
        name="reference_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(ReferenceUpdateView.as_view()),
        name="reference_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(ReferenceDeleteView.as_view()),
        name="reference_delete"),

    url(r'^(?P<pk>\d+)/$',
        ReferenceDetailView.as_view(),
        name="reference_detail"),

    url(r'^$',
        ReferenceListView.as_view(),
        name="reference_list"),
)
