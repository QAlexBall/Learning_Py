import numpy as np
# print(np.array) # output: <built-in function array>
print(np.array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0))
''' 
	object 任何暴露数组接口方法的对象都会返回一个数组或任何(嵌套)序列
	dtype 数组的所需数据类型, 可选
	copy 可选, 默认为true, 对象是否可被复制
	order C(按行), F(按列) 或 A(任意, 默认).任意
	subok 默认情况下, 返回的数组被强制为基类数组, 如果为true, 则返回子类
	ndmin 指定返回数组的最小维度
'''
# example 1
a = np.array([1, 2, 3])
print(a) # output: [1 2 3]
# example 2
# 对于一个维度
a = np.array([[1, 2], [3, 4]])
print(a) # output: [[1,2]
		 # 			[3, 4]]
# example 3
# 最小维度
a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a) # output: [[1 2 3 4 5]]
# example 4
a = np.array([1, 2, 3], dtype=complex)
print(a) # output: [ 1.+0.j  2.+0.j  3.+0.j]

'''
ndarry对象由计算机内存中的一位连续区域组成, 带有将每个元素映射到内存块中
某个位置的索引方案, 内存块以按行(C风格)或按列(FORTRAN或MatLab风格)的方式保存元素
'''
