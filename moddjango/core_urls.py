from django.conf.urls import patterns, include, url

urlpatterns = patterns('moddjango.views',
    url(r'^management/$', 'management',  name='management'),
    url(r'^$', 'index', name='index'),
)
