from django.conf.urls import patterns, url

from views import *


urlpatterns = patterns('',
    url(r'^$', WordView.as_view(), name='wordview'),
    url(r'^getword/$', GetWordView.as_view(), name='getwordview'),
    url(r'^settings/$', SettingsView.as_view(), name='settingsview'),
    url(r'^savesettings/$', SaveSettingsView.as_view(), name='savesettingsview'),
    url(r'^export/$', ExportView.as_view(), name='exportview'),
)

