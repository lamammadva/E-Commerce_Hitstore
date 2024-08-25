import os
from celery import Celery
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "selphy.settings")
app = Celery("selphy")
app.conf.enable_utc=False
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

    
# celery -A selphy beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
# celery -A selphy worker --pool=solo -l info