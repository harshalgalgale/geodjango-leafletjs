from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geodjango_leafletjs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('waypoints.urls')),
)
