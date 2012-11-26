# Settings for seabirds.net
import os
DEBUG = True

# Need to duplicate these because sitesettings.py will override settings.py
SITE_ROOT = os.path.join(os.path.dirname(__file__),'seabirds')
SITE_NAME = 'Seabirds.net development'
SITE_URL = 'http://localhost:8000'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
###

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'seabirds',
        'USER': 'joel',
        'HOST': 'localhost',
    }
}
