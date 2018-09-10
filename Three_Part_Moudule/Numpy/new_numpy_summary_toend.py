# 切片索引
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:6]) # output: [1 2 3 4 5]

# 对于二维数组,切片方式稍显不同
arr2 = np.array([[1, 2, 3], 
					[4, 5, 6], 
					[7, 8, 9]])
print(arr2[:2])
'''
output:
[[1 2 3]
 [4 5 6]]
'''
print(arr2[:, 1:])
'''
output:
[[2 3]
 [5 6]
 [8 9]]
'''
arr2[1:, 1:] = 0
print(arr2)

# 数组转置和轴对换
arr = np.arange(15).reshape((3, 5))
print(arr)
print(arr.T)
'''
output:
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

[[ 0  5 10]
 [ 1  6 11]
 [ 2  7 12]
 [ 3  8 13]
 [ 4  9 14]]
'''
# 在进行矩阵计算时,经常需要用到转置操作,例如利用np.dot计算矩阵內积
arr = np.random.randn(6, 3)
print(arr)
print(np.dot(arr.T, arr))
'''
output:
[[-1.27395567  0.00955796 -1.28750516]
 [-0.08475422  0.52563736 -2.05030602]
 [ 1.17591993 -0.015422    0.88881672]
 [ 2.15608896  0.27987763 -0.92061775]
 [-0.11040883 -0.82964402 -0.06859076]
 [-1.66814933  0.36754     0.32394515]]

[[  1.04565659e+01   7.06805306e-03   3.41424263e-01]
 [  7.06805306e-03   1.17835017e+00  -1.18542228e+00]
 [  3.41424263e-01  -1.18542228e+00   7.60860167e+00]]
'''
# 对于高维数组, transpose需要得到一个由轴编号组成的元组才能对这些轴进行转置
arr = np.arange(16).reshape((2, 2, 4))
print(arr)
'''
output:
[[[ 0  1  2  3]
  [ 4  5  6  7]]

 [[ 8  9 10 11]
  [12 13 14 15]]]
'''
print(arr.transpose((1, 0, 2))) # 0轴变成了1轴, 1轴换成了0轴, 2轴不变
'''
output:
[[[ 0  1  2  3]
  [ 8  9 10 11]]

 [[ 4  5  6  7]
  [12 13 14 15]]]
'''

print(arr.transpose((1, 2, 0)))
'''
[[[ 0  8]
  [ 1  9]
  [ 2 10]
  [ 3 11]]

 [[ 4 12]
  [ 5 13]
  [ 6 14]
  [ 7 15]]]
'''
# 简单的转置可以使用.T,就是进行轴对换.
# ndarray还有一个swapaxes方法, 它需要接受一个轴编号
print(arr)
'''
output:
[[[ 0  1  2  3]
  [ 4  5  6  7]]

 [[ 8  9 10 11]
  [12 13 14 15]]]
'''
print(arr.swapaxes(1, 2))
'''
output:
[[[ 0  4]
  [ 1  5]
  [ 2  6]
  [ 3  7]]

 [[ 8 12]
  [ 9 13]
  [10 14]
  [11 15]]]
'''
print(arr.transpose(0, 2, 1))
'''
output:
[[[ 0  4]
  [ 1  5]
  [ 2  6]
  [ 3  7]]

 [[ 8 12]
  [ 9 13]
  [10 14]
  [11 15]]]
'''

# 用于数组的文件输入输出
'''
Numpy能够读写次爬上的文本数据或二进制数据.
np.save和np.load是读写磁盘数组数据的两个主要函数.
默认情况下, 数组是以未亚索的原始二进制格式保存在扩展名为.npy文件中的
'''
arr = np.arange(10)
np.save('some_array', arr)
# 如果文件路径末尾没有扩展名.npy,则该扩展名会被自动添加 
#　然后就可以通过np.load读取磁盘上的数组
print(np.load('some_array.npy'))# output: [0 1 2 3 4 5 6 7 8 9]
# 通过np.savez可以将多个数组保存到一个未压缩的文件中, 将数组以关键字参数的形式传入即可
np.savez('array_achive.npz', a=arr, b=arr)
# 加载.npz文件时,会得到一个类似字典的对象,该对象会对各个数组进行延迟加载
arch = np.load('array_achive.npz')
print(dir(arch))
print(arch.items(), '\n', arch['b'])
'''
output:
[('a', array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])), ('b', array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))] 
 [0 1 2 3 4 5 6 7 8 9]
'''
# 如果数据压缩的很好,就可以使用numpy.savez_compressed:
np.savez_compressed('arrays_compressed.npz', a=arr, b=arr.T)
arch = np.load('arrays_compressed.npz')
print(arch['a'])
print('\n')
print(arch['b'])
print(arch['a'] * arch['b'])
