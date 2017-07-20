from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import Post

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'P3.settings')
app = Celery('P3')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@receiver(post_save, sender=Post )
def count_task(self,blog_id): # get blog_id and count all the posts_words
    posts_words = str('')

    return posts_words