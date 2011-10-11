from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns(
    '',
    url("", include("content.urls")),
    # url(r'^blag/', include('blag.foo.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)
