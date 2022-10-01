from django.urls import path

from .views import *


urlpatterns = [
    path(r'', WordView.as_view(), name='wordview'),
    path(r'getword/', GetWordView.as_view(), name='getwordview'),
    path(r'settings/', SettingsView.as_view(), name='settingsview'),
    path(r'savesettings/', SaveSettingsView.as_view(), name='savesettingsview'),
    path(r'export/', ExportView.as_view(), name='exportview'),
]

