# python的os模块可以调用操作系统提供的接口函数
import os
print(os.name)
# print(os.uname()) os模块的某些函数和操作系统相关
# print(os.environ) # 查看操作系统中定义的环境变量
# print()
# print(os.environ.get('PATH')) # 查看path

# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录
os.path.join('.', 'testdir')
# os.mkdir('./testdir')
# 删除一个目录
# os.rmdir('./testdir')

# 把两个路径合成一个时, 不要直接拼接字符串, 通过os.path.join()函数
# 这样可以正确吃力不同操作系统的路径分隔符
# 要拆分路径时, 使用os.path.split()函数
print(os.path.split('./testdir/file.txt'))
# os.path.splitext()可以直接得到文件扩展名
print(os.path.splitext('./testdir/file.txt'))
os.path.splitdrive('./testdir/file.txt')
os.path.splitunc('./testdir/file.txt')
# 文件重名
# os.rename('./testdir/abc.txt', './testdir/abc.py')
# 删除文件
# os.remove('./testdir/abc.py')
# 复制文件不存在os模块中, 它由shutil模块提供
# shutil可以看成是os的补充模块

# 列出当前目录下所有目录
print([ x for x in os.listdir('.') if os.path.isdir(x)])
# 列出当前目录下所有的.py文件
print([ x for x in os.listdir('.') if os.path.isfile(x) 
	and os.path.splitext(x)[1] == '.py'])
