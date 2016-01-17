from django.conf.urls import patterns, url
from ..views import (LoanListView, LoanCreateView, LoanDetailView,
                     LoanUpdateView, LoanDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(LoanCreateView.as_view()),
        name="loan_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(LoanUpdateView.as_view()),
        name="loan_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(LoanDeleteView.as_view()),
        name="loan_delete"),

    url(r'^(?P<pk>\d+)/$',
        LoanDetailView.as_view(),
        name="loan_detail"),

    url(r'^$',
        LoanListView.as_view(),
        name="loan_list"),
)
