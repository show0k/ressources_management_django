from django.conf.urls import patterns, include

urlpatterns = patterns('',

    (r'^categories/', include('flowers_ressources_management.resources.urls.category_urls')),  # NOQA
    (r'^items/', include('flowers_ressources_management.resources.urls.item_urls')),
    (r'^states/', include('flowers_ressources_management.resources.urls.state_urls')),
    (r'^loans/', include('flowers_ressources_management.resources.urls.loan_urls')),
    (r'^references/', include('flowers_ressources_management.resources.urls.reference_urls')),
)
