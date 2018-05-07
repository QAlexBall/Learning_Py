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