import sys

globals().update(vars(sys.modules['main.urls']))

urlpatterns += patterns('',
url(r'^first_post/', include('first_post.urls', namespace='first_post', app_name='first_post')),
url(r'^posts/', include('posts.urls', namespace='posts', app_name='posts')),
	url(r'^moddjango/', include(
	    'moddjango.core_urls',
	    namespace='moddjango',
	    app_name='moddjango')),
)
