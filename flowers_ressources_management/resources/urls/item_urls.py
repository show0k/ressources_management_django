from django.conf.urls import patterns, url
from ..views import (ItemListView, ItemCreateView, ItemDetailView,
                     ItemUpdateView, ItemDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(ItemCreateView.as_view()),
        name="item_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(ItemUpdateView.as_view()),
        name="item_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(ItemDeleteView.as_view()),
        name="item_delete"),

    url(r'^(?P<pk>\d+)/$',
        ItemDetailView.as_view(),
        name="item_detail"),

    url(r'^$',
        ItemListView.as_view(),
        name="item_list"),
)
