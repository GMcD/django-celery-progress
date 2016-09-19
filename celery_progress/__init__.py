from django.conf import settings
# from django.utils.module_loading import import_by_path
from django.utils.module_loading import import_string

BACKEND = getattr(settings, 'CELERY_PROGRESS_BACKEND',
                  'celery_progress.backends.CeleryBackend')


def get_backend():
    return import_string(BACKEND)


backend = get_backend()()
