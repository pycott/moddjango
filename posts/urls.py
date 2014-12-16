from django.conf.urls import patterns, include, url

urlpatterns = patterns('posts.views',
    url(r'^$', 'archive', name='archive'),

    url(r'^detail/(?P<post_id>[\d]+)/$', 'detail', name='detail'),
)
