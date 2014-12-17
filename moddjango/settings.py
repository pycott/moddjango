import sys

globals().update(vars(sys.modules['main.settings']))

MODDJANGO_DIR = os.path.join(BASE_DIR, 'moddjango')
DOWNLOAD_DIR = os.path.join(MODDJANGO_DIR, 'download')
#DOWNLOAD_DIR = '/var/www/rusbiteh-moddjango/moddjango/download/'



INSTALLED_APPS += (
    'moddjango',
)

TEMPLATE_DIRS += (
    os.path.join(BASE_DIR, 'moddjango/templates/'),
)
