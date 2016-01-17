from django.conf.urls import patterns, include

urlpatterns = patterns('',

    (r'^categorys/', include('resources.urls.category_urls')),  # NOQA
    (r'^items/', include('resources.urls.item_urls')),
    (r'^states/', include('resources.urls.state_urls')),
    (r'^loans/', include('resources.urls.loan_urls')),
    (r'^references/', include('resources.urls.reference_urls')),
)
