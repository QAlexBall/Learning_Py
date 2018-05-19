# 用loc和iloc进行选取
# 对于DataFrame的行的标签索引我们引入了特殊的标签运算符loc和iloc.
#　它们可以让你用类似Numpy的标签使用轴标签(loc)或整数索引(iloc), 从DataFrame选择行和列的子集

import pandas as pd
import numpy as np
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

print(data.loc['Colorado', ['two', 'three']])
'''
output:
two      5
three    6
Name: Colorado, dtype: int64
'''
# 然后用iloc和整数进行选取:
print(data.iloc[2, [3, 0, 1]])
'''
output:
four    11
one      8
two      9
Name: Utah, dtype: int64
'''

print(data.iloc[2])
'''
output:
one       8
two       9
three    10
four     11
Name: Utah, dtype: int64
'''
print(data.iloc[[1, 2], [3, 0, 1]])
'''
output:
          four  one  two
Colorado     7    4    5
Utah        11    8    9
'''
# 这两个索引函数也适用与一个标签或多个标签的切片
print(data.loc[:'Utah', 'two'])
'''
output:
Ohio        1
Colorado    5
Utah        9
Name: two, dtype: int64
'''
print(data.iloc[:, :3][data.three > 5])
'''
          one  two  three
Colorado    4    5      6
Utah        8    9     10
New York   12   13     14
'''


