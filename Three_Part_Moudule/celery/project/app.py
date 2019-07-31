from __future__ import absolute_import
from celery import Celery

app = Celery('project', include=['project.tasks'])
app.config_from_object('project.celeryconfg')

if __name__ == '__main__':
    app.start()
