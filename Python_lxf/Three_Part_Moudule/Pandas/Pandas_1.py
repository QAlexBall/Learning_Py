import pandas as pd
# 重新索引
# pandas对象的一个重要方法是reindex,其作用是穿件一个新对象,它的数据符合新的索引.
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)
'''
output:
d    4.5
b    7.2
a   -5.3
c    3.6
dtype: float64
'''
# 用该Series的reindex将会根据新索引进行重排.如果摸个索引当前不存在,就引入缺失值
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)
'''
output:
a   -5.3
b    7.2
c    3.6
d    4.5
e    NaN
dtype: float64
'''
# 对于时间序列这样的有序数据,重新索引可能需要做一些插值处理.
# method选项即可达到此目的,例如,使用ffill可以实现向前值填充
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
obj4 = obj3.reindex(range(6), method='ffill')
print(obj4)
'''
output:
0      blue
2    purple
4    yellow
dtype: object

0      blue
1      blue
2    purple
3    purple
4    yellow
5    yellow
dtype: object
'''

import numpy as np
# 借助DataFrame,reindex可以修改(行)索引和列.只传递一个序列时,会重新索引结果的行
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), 
						index = ['a', 'c', 'd'], 
						columns=['Ohio', 'Texas', 'California'])
print(frame)
'''
output:
   Ohio  Texas  California
a     0      1           2
c     3      4           5
d     6      7           8
'''
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
frame2.index.name = 'state'
frame2.columns.name = 'char'
print(frame2)
'''
output:
char   Ohio  Texas  California
state                         
a       0.0    1.0         2.0
b       NaN    NaN         NaN
c       3.0    4.0         5.0
d       6.0    7.0         8.0
'''
# 列可以用columns关键字重新索引
states = ['Texas', 'Utah', 'California']
print(frame2.reindex(columns=states))
'''
output:
char   Texas  Utah  California
state                         
a        1.0   NaN         2.0
b        NaN   NaN         NaN
c        4.0   NaN         5.0
d        7.0   NaN         8.0
'''

# 丢弃指定轴上的项

obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
'''
a    0.0
b    1.0
c    2.0
d    3.0
e    4.0
dtype: float64
'''

new_obj = obj.drop('c')
print(new_obj)
'''
output:
a    0.0
b    1.0
d    3.0
e    4.0
dtype: float64
'''

print(obj.drop(['d', 'c']))
'''
output:
a    0.0
b    1.0
e    4.0
dtype: float64
'''

# 对于DataFrame,可以删除任意轴上的索引值.
data = pd.DataFrame(np.arange(16).reshape((4, 4)), 
					index=['Ohio', 'Colorado', 'Utah', 'New York'],
					columns=['one', 'two', 'three', 'four'])
print(data)
'''
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
'''
print(data.drop(['Colorado', 'Ohio']))
'''
          one  two  three  four
Utah        8    9     10    11
New York   12   13     14    15
'''

# 通过传递axis=1或axis='columns'可以删除列的值:
print(data.drop('two', axis=1))
print(data.drop(['two', 'four'], axis='columns'))
'''
output:
          one  three  four
Ohio        0      2     3
Colorado    4      6     7
Utah        8     10    11
New York   12     14    15
          one  three
Ohio        0      2
Colorado    4      6
Utah        8     10
New York   12     14
'''

# 许多函数,如drop,会修改Series或DataFrame的大小或形状,可以就地修改对象,不会返回新的对象
obj.drop('c', inplace=True)
print(obj)
'''
output:
a    0.0
b    1.0
d    3.0
e    4.0
dtype: float64
'''

# 索引,选取和过滤
# Series索引(obj[...])的工作方式类似于Numpy数组的索引,只不过Series的索引值不只是整数
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
'''
output:
a    0.0
b    1.0
c    2.0
d    3.0
dtype: float64
'''

print(obj['b']) # output: 1.0
print(obj[1]) # output: 1.0
print(obj[2:4])
'''
output:
c    2.0
d    3.0
dtype: float64
'''

print(obj[['b', 'a', 'd']])
'''
output:
b    1.0
a    0.0
d    3.0
dtype: float64
'''

print(obj[[1, 3]])
'''
output:
b    1.0
d    3.0
dtype: float64
'''

print(obj[obj < 2])
'''
output:
a    0.0
b    1.0
dtype: float64
'''

# 利用标签的切片运算与普通的Python切片运算不同,其末端是包含的
print(obj['b':'d'])
'''
output:
b    1.0
c    2.0
d    3.0
dtype: float64
'''

# 用切片可以对Series的部分进行设置
obj['b':'c'] = 5
print(obj)
'''
output:
a    0.0
b    5.0
c    5.0
d    3.0
dtype: float64
'''

print(data)
print(data['two'])
'''
output:
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
Ohio         1
Colorado     5
Utah         9
New York    13
Name: two, dtype: int64
'''
print(data[['three', 'one']])
'''
output:
          three  one
Ohio          2    0
Colorado      6    4
Utah         10    8
New York     14   12
'''

print(data[:2])
print(data[data['three'] > 5])
print(data < 5)
'''
output:
          one  two  three  four
Ohio        0    1      2     3
Colorado    4    5      6     7
          one  two  three  four
Colorado    4    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
            one    two  three   four
Ohio       True   True   True   True
Colorado   True  False  False  False
Utah      False  False  False  False
New York  False  False  False  False
'''
data[data < 5] = 0
print(data)
'''
output:
          one  two  three  four
Ohio        0    0      0     0
Colorado    0    5      6     7
Utah        8    9     10    11
New York   12   13     14    15
'''