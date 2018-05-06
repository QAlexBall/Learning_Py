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
