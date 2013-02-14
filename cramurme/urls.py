from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'content.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),

    url("", include("content.urls")),
)
urlpatterns += staticfiles_urlpatterns()
