''' 
numpy最终要的特点就是Ｎ维数组对象(ndarray),他是一个快速而领会的大数据集容器
可以对数据执行一些数学运算,其语法和标量元素相同.
'''
from numpy.random import randn
import numpy as np
data = randn(2, 3) # 创建随机数2*3维
print(data)
print(data*10)
print(data + data)
'''
output:
data
[[ 0.26474196  0.39938213  0.00644464]
 [-0.89070803  1.20568504  0.77317617]]

data * 10
[[  2.64741962   3.99382133   0.06444643]
 [ -8.90708032  12.05685039   7.73176167]]

data + data
[[ 0.52948392  0.79876427  0.01288929]
 [-1.78141606  2.41137008  1.54635233]]
'''

'''
需要注意的是ndarray是一个通用的同构数据多维容器, 也就是说**所有元素的类型必须相同**
同时,每个数组都有一个shape(各维大小的元组)属性和一个dtype(用于说明数组数据类型的对象)
'''
arr = [1, '2', 'a', 'c']
d = np.array(arr) # 会把数组中不同类型的元素转换成相同类型
print(d)
'''
output:
['1' '2' 'a' 'c']
'''
print(d.shape, d.dtype)
'''
output:
(4,) <U21
'''

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]] # 创建多维数组
arr2 = np.array(data2) # 转换成多维
print(arr2.ndim, arr2.shape)
'''
output:
2 (2, 4)
'''

np.zeros(10) # 创建一维10个数据都为0的数组
np.zeros((3, 6)) # 创建一个3*6数据都为0的数组
np.empty((2, 3, 2)) # 创建2*3*2的数组

'''
创建数组函数
array 		将输入数据转换为ndarray.

asarray 	将输入数据转换为ndarray.

arange		类似内置range.返回ndarray

ones,		根据指定的形状和dtype创建一个全1的数组.
ones_like	ones_like以另一个数组为参数, 并根据器形状和dtype创建一个全1的数组

zeros
zeros_like 	类似上一个

empty
empty_like 	同上

eye,
identity	穿件一个N*N单位矩阵(对角线为1, 其余为0)
'''

# ndarray的type可以显示转换
array = np.array([1, 2, 3, 4, 5])
float_arr = array.astype(np.float64)	# 整形转换为浮点型
print(float_arr.dtype)
'''
output:
float64
'''

array = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
array = array.astype(np.int32) # 浮点型转换为整型(小数部分被截断)
print(array)
'''
output:
[ 3 -1 -2  0 12 10]
'''

'''
### 数组与标量之间的运算
数组可以不用编写循环就可以对数据进行批量运算(也就是矢量化).
大小相同的数组运算会将运算应用到元素级
'''
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
'''
output:
[[ 1.  2.  3.]
 [ 4.  5.  6.]]
'''
print(arr * arr)
''' 
output:
[[  1.   4.   9.]
 [ 16.  25.  36.]]
'''

# 同样的,数组与标量间的计算也会传播到元素级(不同大小的数组运算叫广播)
print(1 / arr)
''' 
output:
[[ 1.          0.5         0.33333333]
 [ 0.25        0.2         0.16666667]]
'''

'''
## 基本的切片与索引
类似于python内置的list和tuple

### 花式索引
花式索引是numpy的术语, 他是利用整数数组进行索引
'''
arr = np.empty((8, 4))
for i in range(8):
	arr[i] = i
print(arr)
'''
output:
[[ 0.  0.  0.  0.]
 [ 1.  1.  1.  1.]
 [ 2.  2.  2.  2.]
 [ 3.  3.  3.  3.]
 [ 4.  4.  4.  4.]
 [ 5.  5.  5.  5.]
 [ 6.  6.  6.  6.]
 [ 7.  7.  7.  7.]]
'''
print(arr[[4, 3, 0, 6, 5]]) # 选取索引为4, 3, 0, 6, 5的行
'''
output:
[[ 4.  4.  4.  4.]
 [ 3.  3.  3.  3.]
 [ 0.  0.  0.  0.]
 [ 6.  6.  6.  6.]
 [ 5.  5.  5.  5.]]
'''
print(arr[[-1, -5]])
'''
output:
[[ 7.  7.  7.  7.]
 [ 3.  3.  3.  3.]]
'''

# 一次性传入多个索引会返回一个一维数组
arr = np.empty((8, 4))
for i in range(1, 9):
	for j in range(1, 5):
		arr[i-1][j-1] = i * j
print(arr)
'''
output:
[[  1.   2.   3.   4.]
 [  2.   4.   6.   8.]
 [  3.   6.   9.  12.]
 [  4.   8.  12.  16.]
 [  5.  10.  15.  20.]
 [  6.  12.  18.  24.]
 [  7.  14.  21.  28.]
 [  8.  16.  24.  32.]]
 '''
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]]) # 返回(1, 0), (5, 3), (7,1), (2, 2)这四个元素
# output: [  2.  24.  16.   9.]

print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]) # 以返回(1, 0), (1, 3), (1, 1), (1, 2)
											#	 (5, 0), ...
											#	 (7, 0), ...
											#	 (2, 0), ...
											# 4*4的数组
'''
output:
[[  2.   8.   4.   6.]
 [  6.  24.  12.  18.]
 [  8.  32.  16.  24.]
 [  3.  12.   6.   9.]]
'''
arr_ix = arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]
print(arr_ix)

'''
output:
[[  2.   8.   4.   6.]
 [  6.  24.  12.  18.]
 [  8.  32.  16.  24.]
 [  3.  12.   6.   9.]]
'''

'''
numpy可以简化数据处理,避免了python写循环,用数组表达式代替循环的做法一般叫矢量化
一般来说,矢量化的运算要比纯Python的循环快上1-2个数量级
在一组树枝上计算(sqrt(x^2 + y^2))
'''
from matplotlib.pyplot import imshow, title
import matplotlib.pyplot as plt
points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points) # np.meshgrid函数接受2个一维5数组,并产生2个二维矩阵(分别对应x和y)
z = np.sqrt(xs ** 2 + ys ** 2)
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
# plt.show()

# 将条件逻辑表述为数组运算
# numpy.where函数是三元表达式x if condition else y的矢量版本
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
# 需要判断cond中的值为True时选取xarr, 为False时选取yarr
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)] # python版本
result = np.where(cond, xarr, yarr)
print(result)
'''
output:
[ 1.1  2.2  1.3  1.4  2.5]
'''
# np.where的第二个和第三个参数不一定是数组,它们可以是标量值.
# 在数据分析中,where通常用于根据一个数组产生另一个数组.

# 假设有一个由随机数数据组成的矩阵,希望把所有大于0的值替换为2, 小于0的值替换为-2
arr = randn(4, 4)
np.where(arr > 0, 2, -2) # 大于0为2, 小于0为-2
np.where(arr > 0, 2, arr)# 大于0为2, 小于0不变
# 传给where的数组大小可以不相等,甚至可以是标量
'''
result = []
for i in range(n):
	if cond1[i] and cond2[i]:
		result.append(0)
	elif cond1[i]:
		result.append(1)
	elif cond2[i]:
		result.append(2)
	else:
		result.append(3)
# python原始实现
np.where(cond1 & cond2, 0, p.where(cond2, np.where(2, 3)))
resutlt = 1 * cond1 + 2 * cond2 + 3 * -(cond1 | cond2)
'''
# 数学和统计方法
# sum, mean以及标准差std等聚合计算可以当所数组的方法使用,也可以当做numpy函数使用
arr = np.random.randn(5, 4) # 正态分布的数据
print(arr)
print(arr.mean())
print(arr.mean() * 20)
print(arr.sum())
'''
output:
-0.391861236317
-7.83722472633
-7.83722472633
'''
arr = np.zeros((2, 6))
print(arr)
print(arr.mean(axis=0), '\n') # 0求每一列平均
print(arr.mean(axis=1), '\n') # 1求每一行平均
#print(arr.mean(axis=2), '\n')

print(arr.sum(0))

