from django.conf.urls import patterns, include, url

from tastypie.api import Api

from emberplay.api import UserResource, MessageResource

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

v1_api = Api(api_name='1')
v1_api.register(UserResource())
v1_api.register(MessageResource())


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'emberplay.views.index', name='index'),
    url(r'^index.html$', 'emberplay.views.index'),

    # url(r'^emberplay/', include('emberplay.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
