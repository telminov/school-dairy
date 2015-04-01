from django.conf.urls import include, url
from django.contrib import admin
import djutils.views.rest_auth

urlpatterns = [
    url(r'^', include('dairy.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/auth/login/$', djutils.views.rest_auth.login),
    url(r'^api/auth/logout/$', djutils.views.rest_auth.logout),
    url(r'^api/auth/current_user/$', djutils.views.rest_auth.get_current_user),
]
