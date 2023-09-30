from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'R4C.settings')

app = Celery('R4C')
app.conf.enable_utc = False

app.config_from_object(settings, namespace='CELERY')

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")

app.autodiscover_tasks()
