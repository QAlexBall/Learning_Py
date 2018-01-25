""" 
python的字符串类型为str,在内存中以Unicode表示, 一个字符对应若干个字节.在内存中以Unicode表示
如果要在网络上传输,或者保存到磁盘上,就需要把str变为一字节为单位的bytes. 
"""

print(ord('A'), chr(66), ord('中'))
x = b'ABC'
print('中午'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe5\x8d\x88'.decode('utf-8'))
print(x)
print(len('ABC'), len('中文'), len('中文'.encode('utf-8')))

"""
len函数计算的是str的字符数, 如果换成bytes, len()函数就得计算字节数:
"""
print(len(b'ABC'))

"""
输出格式化字符串
常见占位符 %d整数 %f浮点数 %s字符串 %x十六进制数
%s 可以将所有类型转化为字符串
"""
x = 100
print('hello, %s, %d' % ('world', x))
print('Hi, %s, you hava $%d' % ('Michael', 100000000))




