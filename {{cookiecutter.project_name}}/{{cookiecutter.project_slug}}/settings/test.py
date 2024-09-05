from .base import *

# region GENERAL ---------------------------------------------------------------

DEBUG = True

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# endregion --------------------------------------------------------------------

# region DATABASES -------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# endregion --------------------------------------------------------------------

# region PASSWORDS -------------------------------------------------------------

PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']

# endregion --------------------------------------------------------------------

# region CACHES ----------------------------------------------------------------

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '',
    },
}

# endregion --------------------------------------------------------------------
