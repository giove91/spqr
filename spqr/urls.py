from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic.base import RedirectView

from words import views


urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(pattern_name='wordview', permanent=False)),
    url(r'^words/', include('words.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^account/passwordchange/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^account/passwordchangedone/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^account/logout/$', views.logout_view, name='logout'),
)

