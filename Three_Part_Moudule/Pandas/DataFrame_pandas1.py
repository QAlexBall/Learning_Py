# DataFrame是一个表格类型的数据结构,它含有一组有序的列,每列可以是不同的值类型(数值,字符串,布尔值)等.
# DataFrame既有行索引也有列索引,它可以被看做是由Series组成的字典(共用同一个索引).
# DataFrame中的数据是以一个或多个二维存放的(而不是列表,字典或别的一维数据结构).
'''
虽然DataFrame是以二维结构保存数据的,但仍然可以轻松地将其表示为更高维的数据
(层次化索引的表格型结构, 这是pandas中许多高级数据处理功能的关键要素)
'''

# 建DataFrame的办法有很多,最常用的一种是直接传入一个由等长列表或Numpy数组组成的字典
import pandas as pd
from pandas import DataFrame
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'], 
		'year': [2000, 2001, 2002, 2001, 2002, 2003],
		'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)
'''
output:
   pop   state  year
0  1.5    Ohio  2000
1  1.7    Ohio  2001
2  3.6    Ohio  2002
3  2.4  Nevada  2001
4  2.9  Nevada  2002
5  3.2  Nevada  2003
'''
# 对于特别大的DataFrame, head()方法会选取前五行
print(frame.head())
'''
output:
   pop   state  year
0  1.5    Ohio  2000
1  1.7    Ohio  2001
2  3.6    Ohio  2002
3  2.4  Nevada  2001
4  2.9  Nevada  2002
'''
# 如果指定了列序列,则DataFrame的列就会按照指定顺序进行排列
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))
'''
output:
   year   state  pop
0  2000    Ohio  1.5
1  2001    Ohio  1.7
2  2002    Ohio  3.6
3  2001  Nevada  2.4
4  2002  Nevada  2.9
5  2003  Nevada  3.2
'''
# 如果传入的列在数据中找不到,就会在结果中产生缺失值
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], 
	index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame2)
print(frame2.columns)
'''
output:
       year   state  pop debt
one    2000    Ohio  1.5  NaN
two    2001    Ohio  1.7  NaN
three  2002    Ohio  3.6  NaN
four   2001  Nevada  2.4  NaN
five   2002  Nevada  2.9  NaN
six    2003  Nevada  3.2  NaN
Index(['year', 'state', 'pop', 'debt'], dtype='object')
'''

# 通过类似字典标记的方法或属性的方式，可以将DataFrame的列获取为一个Series
print(frame2['state'])
print(frame2.year)
'''
output:
one        Ohio
two        Ohio
three      Ohio
four     Nevada
five     Nevada
six      Nevada
Name: state, dtype: object
one      2000
two      2001
three    2002
four     2001
five     2002
six      2003
Name: year, dtype: int64
'''
# 列可以通过赋值的方式进行修改.
frame2['debt'] = 16.5
print(frame2)
'''
output:
       year   state  pop  debt
one    2000    Ohio  1.5  16.5
two    2001    Ohio  1.7  16.5
three  2002    Ohio  3.6  16.5
four   2001  Nevada  2.4  16.5
five   2002  Nevada  2.9  16.5
six    2003  Nevada  3.2  16.5
'''
import numpy as np
frame2['debt'] = np.arange(6.)
print(frame2)
'''
output:
       year   state  pop  debt
one    2000    Ohio  1.5   0.0
two    2001    Ohio  1.7   1.0
three  2002    Ohio  3.6   2.0
four   2001  Nevada  2.4   3.0
five   2002  Nevada  2.9   4.0
six    2003  Nevada  3.2   5.0
'''

frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)
'''
output:
       year   state  pop  debt  eastern
one    2000    Ohio  1.5   0.0     True
two    2001    Ohio  1.7   1.0     True
three  2002    Ohio  3.6   2.0     True
four   2001  Nevada  2.4   3.0    False
five   2002  Nevada  2.9   4.0    False
six    2003  Nevada  3.2   5.0    False
'''
# del方法可以删除列
del frame2['eastern']
print(frame2.columns)
'''
output:
Index(['year', 'state', 'pop', 'debt'], dtype='object')
'''

'''
注意: 通过索引方式返回的列只是响应数据的视图, 并不是副本.
因此,对返回Series所做的任何就地修改全都会反应到源DataFrame上.
通过copy方法即可指定复制列
'''
# 另一种常见数据形式是嵌套字典
pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 
		'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
# 如果嵌套字典传给DataFrame,pandas就会被解释: 外层字典的键作为列,内层键则作为行索引
frame3 = pd.DataFrame(pop)
print(frame3)
'''
output:
      Nevada  Ohio
2000     NaN   1.5
2001     2.4   1.7
2002     2.9   3.6
'''
# 可以用类似Numpy数组的方法,对DataFrame进行转置
print(frame3.T)
'''
output:
        2000  2001  2002
Nevada   NaN   2.4   2.9
Ohio     1.5   1.7   3.6
'''
# 内层字典的键会被合并,排序以形成最终的索引.
print(pd.DataFrame(pop, index=[2001, 2002, 2003]))
'''
output:
      Nevada  Ohio
2001     2.4   1.7
2002     2.9   3.6
2003     NaN   NaN
'''

# 由Series组成的字典差不多也是一样的用法
pdata = {'Ohio': frame3['Ohio'][:1], 
			'Nevada': frame3['Nevada'][:2]}
print(pd.DataFrame(pdata))
'''
output:
      Nevada  Ohio
2000     NaN   1.5
2001     2.4   NaN
'''

# 如果设置了DataFrame的index和columns的name属性, 则这些信息也会被显示出来
frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)
'''
output:
state  Nevada  Ohio
year               
2000      NaN   1.5
2001      2.4   1.7
2002      2.9   3.6
'''
print(frame3.values)
'''
output:
[[ nan  1.5]
 [ 2.4  1.7]
 [ 2.9  3.6]]
'''

print(frame2.values)
'''
output:
[[2000 'Ohio' 1.5 0.0]
 [2001 'Ohio' 1.7 1.0]
 [2002 'Ohio' 3.6 2.0]
 [2001 'Nevada' 2.4 3.0]
 [2002 'Nevada' 2.9 4.0]
 [2003 'Nevada' 3.2 5.0]]
'''

# 索引对象
# pandas的索引对象负责管理轴标签和其它元数据(比如轴名称等).
#　构建Series或DataFrame时, 所用到的任何数组或其他序列的标签都会被转换成一个index
obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index)
print(index[1:])
'''
output:
Index(['a', 'b', 'c'], dtype='object')
Index(['b', 'c'], dtype='object')
'''

# Index对象是不可变的,因此用户不能对其进行修改:
#　Error index[1] = 'd'
# 不可变可以使的Index对象在多个数据结构之间安全共享

labels = pd.Index(np.arange(3))
print(labels) # output: Int64Index([0, 1, 2], dtype='int64')
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print(obj2)
'''
output:
0    1.5
1   -2.5
2    0.0
dtype: float64
'''
print(obj2.index is labels) #　output: True

'''
注意: 虽然用户不需要经常使用Index功能但是因为一些操作会生成
包含被索引化的数据,理解它们的工作原理是很重要的
'''

#　除了类似于数组，Index的功能也类似一个固定大小的集合
print(frame3)
'''
output:
state  Nevada  Ohio
year               
2000      NaN   1.5
2001      2.4   1.7
2002      2.9   3.6
'''
print(frame3.columns) # output: Index(['Nevada', 'Ohio'], dtype='object', name='state')
print('Ohio' in frame3.columns) # output: True
print(2003 in frame3.index)  # output: False

# 与python的集合不同, pandas的Index可以包含重复的标签
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
print(dup_labels) # output: Index(['foo', 'foo', 'bar', 'bar'], dtype='object')
