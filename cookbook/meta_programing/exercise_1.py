"""
exercise 1
"""
import time
import logging
from functools import wraps


def timethis(func):
    """
    Decorator that reports the execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(num):
    """
    Counts down
    """
    while num > 0:
        num -= 1


def logged(level, name=None, message=None):
    """
    logged
    """
    def decorate(func):
        logname = name if name else func.__module__
        print(logname)
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


print(add(1, 2))
spam()

countdown(100)
countdown(1000)
countdown(10000000)
