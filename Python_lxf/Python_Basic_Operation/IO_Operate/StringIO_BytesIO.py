# StringIO and BytesIO
# StringIO 就是在内存中读写str.
# 要把str写入StringIO, 先创建一个StringIO,
# 然后, 像文件一样写入
from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.getvalue())
print(f.write(', world!'))
print(f.getvalue())


# 要读取StringIO, 可以用一个str初始化StringIO
from io import StringIO
f = StringIO('Hello!\nHi\nGoodbye!') # 用一个str初始化StringIO
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())

# BytesIO实现了在内存中读写bytes
from io import BytesIO
f = BytesIO()
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())
# 和StringIO一样可以用一个bytes初始化BytesIO, 然后读取
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

