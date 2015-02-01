from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^subscribe/', 'subscribe.views.index'),
    url(r'^admin/', include(admin.site.urls)),

    # Login
    #url(r'^accounts/login/$', 'login.views.login'),
    #url(r'^accounts/auth/$', 'login.views.auth_view'),
    #url(r'^accounts/logout/$', 'login.views.logout'),
    #url(r'^accounts/loggedin/$', 'login.views.loggedin'),
    #url(r'^accounts/invalid/$', 'login.views.invalid_login'),
) 
