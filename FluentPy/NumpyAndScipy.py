import numpy

a = numpy.arange(12)
print(a)
print(type(a))
print(a.shape)
a.shape = 3, 4
print(a)
print(a[2])
print(a[2, 1])
print(a[:, 1])
print(a.transpose())

# Numpy也可以对numpy.ndarray 中的元素进行抽象的读取,保存和其他操作
