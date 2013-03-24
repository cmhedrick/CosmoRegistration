import os

# Import the proper settings_[environment].py file (defaults to dev)
DJANGO_ENVIRONMENT = os.environ.get('DJANGO_ENVIRONMENT', 'dev')
exec('from settings_%s import *' % DJANGO_ENVIRONMENT)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
    'cosmetologyregistry.views.nextapt_context',
    'django.core.context_processors.request',
)
