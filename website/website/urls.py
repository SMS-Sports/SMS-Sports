from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^blog/', include('blog.urls')),
    
    # Subscription choice
    url(r'^subscribe/', 'subscribe.views.index'),

    # Login
    url(r'^login/', 'login.views.login'),
    url(r'^auth/', 'login.views.auth_view'),
    url(r'^logout/', 'login.views.logout'),
    url(r'^loggedin/', 'login.views.loggedin'),
    url(r'^invalid/', 'login.views.invalid_login'),
) 
