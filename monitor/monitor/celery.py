from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitor.settings')

app = Celery('monitor')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete': {
        'task': 'api.tasks.delete_undefined_data',
        # every 300 secs (5 min)
        'schedule': 300,
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
