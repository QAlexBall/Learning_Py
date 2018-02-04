# Simple FileWR
# 读文件
f = open('File/a.txt', 'r')
print(f)
# 调用read()方法可以一次都去文件全部内容
# 调用read会一次性读取文件的全部内容, 可以反复调用read(size)方法,
# 每次最多读取size个字节的内容, 也可以调用readline(),每次读取一行内容
# readlines()一次读取所有内容并返回list.
# 一般情况下, 如果文件很小使用read(), 如果不能确定其大小反复调用(read(size))
# 如果是配置文件使用readlines()
print(f.read(2), '\t', f.readline(), f.readline())
print(f.read())
# 最后一步调用是关闭文件
print(f.close())
print()

try:
	f = open('File/a.txt', 'r')
	print(f.read())
finally:
	if f:
		f.close()
		print()
# 这和前面的try...finally是一样的, 并且不必调用f.close()方法
with open('File/a.txt', 'r') as f:
	print(f.readline())
	for line in f.readlines():
		print(line.strip())

# file like object
# open()函数返回的这种有read()方法的对象, 在python中统称为
# file-like object. 除了file外, 还可以是内存的字节流, 网络流, 自定义流等等
# file-like object不需求从特定类继承, 只要写个read()方法就行
# StringIO就是在内存中创建的file-like object, 常用作临时缓冲. 

# 二进制文件
f = open('File/a.jpg', 'rb')
print(f.read(2))
print(f.readline())
# 字符编码
# 如果遇到编码错误, 可以接收errors参数
f = open('File/gbk.txt', 'r', encoding='gbk', errors='ignore')
print(f.read())


# 写文件
f = open('File/b.txt', 'w')
# 写文件传入标识符是'w'或者'wb'表示写文本文件或写二进制文件
# r+表示可读写
f.write('Hello, world!!!')
f.close() # 只有调用close()方法时, 操作系统才保证把没有写入的数据全部写入磁盘
with open('File/b.txt', 'w') as f:
	f.write('hello, nihao!')
with open('File/b.txt', 'r') as f:
	print(f.read())
