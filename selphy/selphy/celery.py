import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','selphy.settings')
app = Celery('selphy')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



# celery -A selphy beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
# celery -A selphy worker --pool=solo -l info