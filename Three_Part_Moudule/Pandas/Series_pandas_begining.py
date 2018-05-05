'''
Pandas有两个主要的数据结构: Series和DataFrame

Series是一种类似于一组数组的对象, 它是由一组数据(各种NumPy数据类型)以及一组
与之相关的数据标签(即索引)组成.仅由一组数据即可产生最简单的Series:
'''
import pandas as pd
from pandas import Series, DataFrame
obj = pd.Series([4, 7, -5, 3])
print(obj)
'''
output
0    4
1    7
2   -5
3    3
dtype: int64
'''

'''
Series的字符串表现形式为: 索引在左边, 值在右边.
由于没有为数据指定索引, 于是为自动创建一个0到N-1(N为数组的长度)的整数型索引.
可以通过Series的values和index属性获取其数组表示形式和索引对象.
'''
print(obj.values)
# output: [ 4  7 -5  3]
print(obj.index)
# output: RangeIndex(start=0, stop=4, step=1)
# 通常,我们希望所创建的Series带有一个可以对各个数据点进行标记的索引
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
'''
output:
d    4
b    7
a   -5
c    3
'''
# 与普通numpy数组相比,可以通过索引的方式选取Series中的一个单词或一组值
print(obj2['a']) # output: -5
print(obj2[['a', 'b', 'c']])
'''
output:
a   -5
b    7
c    3
dtype: int64
'''
obj2['d'] = 6
print(obj2[obj2 > 0])
'''
output:
d    6
b    7
c    3
dtype: int64
'''