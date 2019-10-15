"""
collections.namedtuple()函数通过使用一个普通的元组对象，使得可以使名称来访问列表或者元组中的元素
"""

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('alex@me.com', '2019-10-10')
print(sub)
print(sub.addr)
print(sub.joined)

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


s = Stock('ACME', 100, 123.45)
print(s)
