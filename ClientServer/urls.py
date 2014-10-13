from django.conf.urls import patterns, include, url
from login_app.views import login_view, auth_and_login
from sort_app.views import sort
# from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', login_view, name='homepage'),
    url(r'^login/$', auth_and_login),
    url(r'^sort/$', sort),
    url(r'^logout/$', 'django.contrib.auth.views.logout',  {'next_page': 'homepage'}),
    # url(r'^$', 'ClientServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
