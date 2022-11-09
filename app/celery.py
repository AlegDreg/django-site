#import os
#from asgiref.sync import sync_to_async
#from django.apps import apps 
#from celery import Celery

## Set the default Django settings module for the 'celery' program.
##os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RemangaTestTask.settings')

##os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
#app = Celery ('app')
#app.config_from_object('django.conf:settings', namespace='CELERY')

## Using a string here means the worker doesn't have to serialize
## the configuration object to child processes.
## - namespace='CELERY' means all celery-related configuration keys
## should have a `CELERY_` prefix.
##app.config_from_object('django.conf:settings', namespace ='CELERY')

## Load task modules from all registered Django apps.
#app.autodiscover_tasks()