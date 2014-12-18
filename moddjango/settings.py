import sys

globals().update(vars(sys.modules['main.settings']))

MODDJANGO_DIR = os.path.join(BASE_DIR, 'moddjango')
DOWNLOAD_DIR = os.path.join(MODDJANGO_DIR, 'download')
#SERVER_REBOOT_CMD = 'touch ../.touch/rusbiteh-moddjango'
SERVER_REBOOT_CMD =''


INSTALLED_APPS += (
'first_post',
'posts',
    'moddjango',
)

TEMPLATE_DIRS += (
os.path.join(BASE_DIR, 'first_post/templates/'),
os.path.join(BASE_DIR, 'posts/templates/'),
    os.path.join(BASE_DIR, 'moddjango/templates/'),
)
