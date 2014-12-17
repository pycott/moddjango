import sys

globals().update(vars(sys.modules['main.urls']))

urlpatterns += patterns('',
	url(r'^moddjango/', include(
	    'moddjango.core_urls',
	    namespace='moddjango',
	    app_name='moddjango')),
)
