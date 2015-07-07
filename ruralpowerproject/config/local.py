# -*- coding: utf-8 -*-
'''
Local Configurations

- Runs in Debug mode
- Uses console backend for emails
- Use Django Debug Toolbar
'''
from configurations import values
from .common import Common


class Local(Common):

    # DEBUG
    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = DEBUG
    # END DEBUG

    # INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    # END INSTALLED_APPS

    # Mail settings
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')
    # End mail settings

    # django-debug-toolbar
    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar', 'django_extensions',)

    # A tuple of IP addresses, as strings, that:
    # - See debug comments, when DEBUG is True
    # - Receive X headers in admindocs if the XViewMiddleware is installed (see The Django admin documentation generator)
    INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)

    DEBUG_TOOLBAR_CONFIG = {
        'DISABLE_PANELS': [
            'debug_toolbar.panels.redirects.RedirectsPanel',
        ],
        'SHOW_TEMPLATE_CONTEXT': True,
    }
    # end django-debug-toolbar

    # Your local stuff: Below this line define 3rd party library settings
