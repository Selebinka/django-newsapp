import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsapp.settings')

app = Celery('newsapp')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    'get_news': {
        'task': 'news.tasks.get_news',
        'schedule': crontab(minute=0, hour=2),
    },
}


