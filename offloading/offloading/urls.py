from django.conf.urls import patterns, include, url
from django.contrib import admin
from offloading.api.resources import v1_api
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
