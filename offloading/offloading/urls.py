from django.conf.urls import patterns, include, url
from django.contrib import admin
from offloading.api.resources import IncidentResource


incident_resource = IncidentResource()

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include(incident_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
