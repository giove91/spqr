from django.conf.urls import patterns, url

from views import *


urlpatterns = patterns('',
    url(r'^$', WordView.as_view(), name='wordview'),
    url(r'getword/$', GetWordView.as_view(), name='getwordview'),
)

