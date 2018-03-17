'''
数据类型对象描述了对应于数组的固定内存块的解释, 取决于一下方面:
	数组类型(整数, 浮点或Python对象)
	数据大小
	字节序(小端或大端)
	在结构类型的情况下, 字段的名称, 每个字段的数据类型, 和每个字段占用的内存块部分
	如果数据类型是子序列, 他的形状和数据类型

字节顺序取决于数据类型的前缀<或>.<意味着编码是小端(最小的有效字节存储在最小地址中)
.>意味着编码是大端(最大的有效地址存储在最次奥地址中)
'''

import numpy as np
# dtype可由以下语法构建
np.dtype(object, align=True, copy=True)
'''
	object 被转换为数据类型的对象
	align 如果true,则向字段添加间隔, 使其类似于C的结构体
	copy 生成dtype对象的新副本, 如果为flase, 结果是内建数据类型对象的引用
'''

# example 1
dt = np.dtype(np.int32)
print(dt)
# example 2
# int8, int16, int32, int64可以替换为等价的字符串'i1', 'i2', 'i4'以及其他
dt = np.dtype('i8')
print(dt)
# example 3
# 使用端号标记
dt = np.dtype('>i4')
print(dt)
# example 4
dt = np.dtype([('age', np.int8)])
print(dt)
# example 5
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20, ), (30,)], dtype=dt)
print(a)
# example 6
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20, ), (30,)], dtype=dt)
print(a['age'])
# example 7
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('mark', 'f4')])
print(student)
# example 8
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('mark', 'f4')])
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a)
'''
每个内建类型都有一个唯一定义它的字符代码
	'b': 布尔型
	'i': 符号整数
	'u': 无符号整数
	'f': 浮点
	'c': 负数浮点
	'm': 时间间隔
	'M': 日期时间
	'O': Python对象
	'S', 'a': 字符串
	'U': Unicode
	'V': 原始数据(void)
'''