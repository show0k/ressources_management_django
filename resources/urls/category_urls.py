from django.conf.urls import patterns, url
from ..views import (CategoryListView, CategoryCreateView, CategoryDetailView,
                     CategoryUpdateView, CategoryDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',

    url(r'^create/$',  # NOQA
        login_required(CategoryCreateView.as_view()),
        name="category_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CategoryUpdateView.as_view()),
        name="category_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CategoryDeleteView.as_view()),
        name="category_delete"),

    url(r'^(?P<pk>\d+)/$',
        CategoryDetailView.as_view(),
        name="category_detail"),

    url(r'^$',
        CategoryListView.as_view(),
        name="category_list"),
)
