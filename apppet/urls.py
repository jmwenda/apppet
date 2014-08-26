from django.conf.urls import patterns, include, url
from tastypie.api import Api
from apppet.api import StatusResource, AnimalResource, RegisterResource
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(StatusResource())
v1_api.register(AnimalResource())
v1_api.register(RegisterResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apppet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
