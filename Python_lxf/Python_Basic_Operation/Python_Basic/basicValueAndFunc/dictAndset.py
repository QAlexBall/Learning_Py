# -*- coding: utf-8 -*-
"""
python内置了字典: dict的支持, dict全称dictionary, 在其他语言中也成为map,
使用键-☞(key-value)存储, 具有极快的查找速度.
dict 的key是不可变对象
"""

name = ['michael', 'bob', 'tracy']
score = [95, 75, 85]

d = {'michael': 95, 'bob': 75, 'tracy': 85}
d['adam'] = 67
d['jack'] = 90
d['jack'] = 88
# delete key use pop(key)
d.pop('bob')
# d['jafdkfj'] not exist
print(d)
print(d['michael'], d['adam'])
print('thomas' in d) 
# -*- coding: utf-8 -*-

d[(1, 2, 3)] = 1000
# d[(1, [2, 3])] = 2000 error
print(d)

"""
set和dict类似, 也是一组key的集合, 但不存储key.由于key不能重复,
所以在set中,没有重复的key
"""
# 创建一个set需要提供一个list作为输入集合
s = set([1, 2, 3,33, 1, 2, 3, 6])
s.add(1)
s.add(66)
s.remove(33)
print(s)
# set可以看作数学上的无序和无重复的集合, 因此,两个set可以做
# 数学意义上的交集, 并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print((s1 & s2), '\n', (s1 | s2))

# 对不变对象来说,调用对象自身的任意放法, 也不会改变该对象自身的内容
# 相反, 这些方法会创建新的对象并返回, 这样就保证了不可变对象本身永远不可变
a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
print(a.replace('a', 'A'))
print(a)

assert 1 in [1, 2, 3]


