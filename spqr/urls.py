from django.contrib.auth.views import login, password_change, password_change_done
from django.urls import include, path
from django.contrib import admin

from django.views.generic.base import RedirectView

from words import views


urlpatterns = [
    path(r'', RedirectView.as_view(pattern_name='wordview', permanent=False)),
    path(r'words/', include('words.urls')),
    path(r'admin/', admin.site.urls),
    # path(r'account/login/', login, name='login'),
    path(r'account/passwordchange/', password_change, name='password_change'),
    path(r'account/passwordchangedone/', password_change_done, name='password_change_done'),
    path(r'account/logout/', views.logout_view, name='logout'),
]
