from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.9330, (35.6897222, 139.691667))
print(tokyo)

fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits), sorted(fruits, reverse=True), sorted(fruits, key=len))
fruits.sort()
print(fruits)

# 用bisect来管理已排序的序列
"""
bisect模块包含两个主要函数,bisect和insort, 两个函数都利用二分查找算法来在有序数列中查找或插入元素
"""

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 24, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}     {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  | '
        print(ROW_FMT.format(needle, position, offset))

if __name__ == '__main__':

    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%3d' % n for n in HAYSTACK))
    demo(bisect_fn)

import random
SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)