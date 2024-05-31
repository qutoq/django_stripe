from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_stripe.settings')

app = Celery('django_stripe')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update(CELERY_BROKER_URL = 'redis://redis:6379/0',
                CELERY_RESULT_BACKEND = 'redis://redis:6379/0',
                CELERY_ACCEPT_CONTENT = ['json'],
                CELERY_TASK_SERIALIZER = 'json',
                CELERY_RESULT_SERIALIZER = 'json',
                CELERY_TIMEZONE = 'UTC')
app.autodiscover_tasks()