import sys


DOWNLOAD_DIR = '/var/www/rusbiteh-moddjango/moddjango/download/'

globals().update(vars(sys.modules['main.settings']))

INSTALLED_APPS += (
    'moddjango',
#    'posts',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'posts/templates/'),
)
