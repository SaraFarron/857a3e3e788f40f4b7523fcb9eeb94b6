import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

app = Celery('server')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# Необходим pip install django-celery-beat и django_celery_beat в INSTALLED_APPS
# запуск та же команда селери только worker -> beat, потом в новой панеле worker
# app.conf.beat_schedule = {
#     'creaating-new-image': {
#         'task': 'core.tasks.function',
#         'schedule': 15.0
#     }
# }
