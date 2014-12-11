import os

try:
    if os.environ['ENVIRONMENT'] == 'dev':
        os.environ['DJANGO_SETTINGS_MODULE'] = 'main.dev_settings'
except KeyError:
    pass
