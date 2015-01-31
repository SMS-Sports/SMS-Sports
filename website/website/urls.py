from django.conf.urls import patterns, include, url
from django.contrib import admin
from testsite.home import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^subscribe/', include('subscribe.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
