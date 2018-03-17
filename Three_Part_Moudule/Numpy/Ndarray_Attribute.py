import numpy as np

# ndarry.shape
# 这一数组属性返回一个包含数组维度的元组,它也可以用于调整数组大小

# example 1
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)

# example 2
# 调整数组大小
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape = (6, 1)
print(a)

# example 3
# Numpy也提供了reshape函数来调整数组大小
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3, 2)
print(b)

# ndarry.ndim
# 返回数组的维度

# example 1
# 等间隔数组的数组
a = np.arange(24)
print(a)

# example 2
# 以为数组
a = np.arange(24)
print('OK!')
print(a.ndim)
# 调整大小
b = a.reshape(2, 4, 3)
print(b, '\n', b.ndim)

# numpy.itemsize
# example 1
# 这一数组属性返回数组中每个元素的字节单位长度
# 数组dtype为int8(一个字节)
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
y = np.array([[1, 2], [3, 4]], dtype=np.int16)
print(x.itemsize, y.itemsize)

# numpy.flags
# ndarray对象拥有以下属性, 这个函数返回了他们的当前值
# 1. C_CONTIGUOUS (C) 数组位于单一的, C风格的连续区段内
# 2. F_ConTIGUOUS (F) 数组位于单一的, Fortran风格的连续区段内
# 3. OWNDATA (O) 数组的内存从其他对象处借用
# 4. WRITEABLE (W) 数据区域可写入, 将它设置为false会
# 								锁定数据, 使其制度
# 5. ALIGNED (A) 数据和任何元素会为硬件适当对齐
# 6. UPDATEIFCOPY (U) 这个数组时另一个数组的副本.
# 				当这个数组释放时, 源数组会由这个数组中的元素更新
# example
import numpy as np
x = np.array([1, 2, 3, 4, 5])
print(x.flags)

