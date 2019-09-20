""" add tasks """
from __future__ import absolute_import, unicode_literals
from .celery import APP


@APP.task
def add(num1, num2):
    """ add two num """
    return num1 + num2


@APP.task
def mul(num1, num2):
    """ mul two num """
    return num1 * num2


@APP.task
def xsum(numbers):
    """ add list of numbers """
    return sum(numbers)
