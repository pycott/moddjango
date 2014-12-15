from django.conf.urls import patterns, include, url


urlpatterns = patterns('moddjango.views',
    url(r'^$', 'index', name='index'),
    url(r'^management/$', 'management',  name='management'),
#    url(r'^posts/', include(
#        'posts.urls',
#        namespace='posts',
#        app_name='posts')),
)
