# python没有专门处理字节的数据类型. 但由于str即是字符串, 又可以表示字节
# 所以, 字节数组=str. 而在c语言中, 我们可以很方便用struct, union来处理字节, 
# 以及字节和int, float的转换
# 在Python中, 如果要把一个32位无符号整数变成字节, 也就是4个长度的bytes

n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)

# python提供了一个struct模块来解决bytes和其他二进制数据类型的转换
import struct
print(struct.pack('>I', 10240099)) # pack的第一个参数是处理指令:
								   # >表示字节顺序是big-endian, 也就是网络序, I表示4字节无符号整数
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')) # unpack把bytes变成相应的数据类型
														 # >IH说明, 后面的bytes依次变为I:
														 # 4字节无符号整数和H: 2字节无符号整数
with open('test.bmp', 'rb') as file:
	print(file.read(30))
# BMP格式采用小端方式存储数据, 文件头的结构按顺序如下
s = b'BM\xde\x1f\x0b\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00\x84\x03\x00\x00\x0e\x01\x00\x00\x01\x00\x18\x00'
# 两个字节: 'BM'表示Windows位图, 'BA'表示OS/2位图
# 一个4字节整数: 表示位图大小; 一个4字节整数: 保留位, 始终为0
# 一个4字节整数: 实际图像的偏移量; 一个4字节整数: Header的字节数;
# 一个4字节整数: 图像宽度; 一个4字节整数: 图像高度;
# 一个2字节整数: 始终为1; 一个2字节整数: 颜色数
# 组合使用unpack读取:
print(struct.unpack('<ccIIIIIIHH', s))
