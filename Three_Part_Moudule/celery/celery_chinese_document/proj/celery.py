""" run celery """
from __future__ import absolute_import, unicode_literals
from celery import Celery

APP = Celery('proj',
             broker='amqp://119.23.33.220:5672',
             backend='amqp://119.23.33.220:5672',
             include=['proj.tasks'])

APP.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    APP.start()
