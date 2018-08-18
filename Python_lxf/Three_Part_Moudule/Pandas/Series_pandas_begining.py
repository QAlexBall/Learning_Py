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

print(obj2 * 2)
'''
output:
d    12
b    14
a   -10
c     6
dtype: int64
'''
import numpy as np
print(np.exp(obj2))
'''
output:
d     403.428793
b    1096.633158
a       0.006738
c      20.085537
dtype: float64
'''
# 还可以将Series看成是一个定长的有序字典,因为它是索引值到数据值的一个映射
# 它可以用在许多原本需要字典参数的函数中
print('b' in obj2) # output: True
print('e' in obj2) # output: False

# 如果数据被存放字一个Python字典中,也可以直接通过这个字典来创建Series
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 6000, 'Utah': 15000}
obj3 = pd.Series(sdata)
print(obj3)
'''
output:
Ohio      35000
Oregon     6000
Texas     71000
Utah      15000
dtype: int64
'''
print(obj3.sort_values())
'''
output:
Oregon     6000
Utah      15000
Ohio      35000
Texas     71000
dtype: int64
'''
# 如果传入一个字典,则结果Series中的索引就是原字典的键(有序排列)
#　可以传入排好序的字典的键以改变顺序
states = ['Califonia', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)
'''
output:
Califonia        NaN
Ohio         35000.0
Oregon        6000.0
Texas        71000.0
dtype: float64
'''
# 用缺失(missing)或NA来表示缺失数据.
# pandas的isnull和notnull函数可以用于检测缺失数据
print(pd.isnull(obj4))
'''
output:
Califonia     True
Ohio         False
Oregon       False
Texas        False
dtype: bool
'''
print(pd.notnull(obj4))
'''
output:
Califonia    False
Ohio          True
Oregon        True
Texas         True
dtype: bool
'''
# Series也有类似的实例方法
print(obj4.notnull())
'''
output:
Califonia    False
Ohio          True
Oregon        True
Texas         True
dtype: bool
'''
# 对于许多应用而言,Series最重要的一个功能是:
# 根据运算的索引标签自动对齐数据
# Series对象本身及其索引都有一个name属性,该属性和pandas其他的相关功能都十分密切
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)
'''
output:
state
Califonia        NaN
Ohio         35000.0
Oregon        6000.0
Texas        71000.0
Name: population, dtype: float64
'''
# Series的索引可以通过赋值的方式就地修改
print(obj)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)
'''
output:
0    4
1    7
2   -5
3    3
dtype: int64
Bob      4
Steve    7
Jeff    -5
Ryan     3
'''