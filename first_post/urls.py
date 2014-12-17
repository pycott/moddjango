from django.conf.urls import patterns, include, url

urlpatterns = patterns('first_post.views',
    url(r'^$', 'index', name='index'),
)

