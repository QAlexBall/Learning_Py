import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


with timethis('counting'):
    n = 100000
    while n > 0:
        n -= 1


@contextmanager
def list_transaction(orig_list):
    working_item = list(orig_list)
    yield working_item
    orig_list[:] = working_item


items = [1, 2, 3]
with list_transaction(items) as working:
    working.append(4)
    working.append(5)
print(items)


# 通常情况下要写一个上下文管理器，需要定义一个类，里面包含一个__enter__()和一个__exit__()方法
class timethis_v1:
    def __init__(self, label):
        self.label = label

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start))


with timethis("hello"):
    num = 100
    while num < 10000:
        num += 1
    print(num)
