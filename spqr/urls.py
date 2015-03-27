from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic.base import RedirectView


urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(pattern_name='wordview', permanent=False)),
    url(r'^words/', include('words.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

