# Python提供了re模块, 包含所有正则表达式的功能,
# 由于Python的字符串本身也用\转义
# 
# s = 'ABC\\-001' python的字符串
# 对应的正则表达式字符串应变为:
# 'ABC\-001'
# 
# 建议使用Python的r前缀, 就不需要考虑转义的问题
# 
# s = r'ABC\-001' python的字符串
# 对应的正则表达式字符串不变
# 'ABC\-001'

# 判断正则表达式是否匹配
# 如果匹配成功返回一个Match对象, 否则返回None
import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-123'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 123'))
# 常见判断方法
test = 'Python1'
if re.match(r'[A-Z][a-z\_]*\d$', test):
	print('ok')
else:
	print('failed')

# 切分字符串
# 用正则表达式切分字符串比固定的字符更灵活
s = 'a b   c'.split(' ')
s1 = re.split(r'\s', 'a b   c')
s2 = re.split(r'\s+', 'a b   c')
print(s, s1, s2)
s = re.split(r'[\s\,\;]+', 'a,b;; c d')
print(s)

# 分组
# 正则表达式由提取子串的功能, 用()表示的就是要提取的分组(group),表示的就是要提取的分组
# ^(\d{3})-(\d{3,8})$分别定义了两个组, 可以直接从匹配的字符串中提取区号和本地号码
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-123')
print(m, m.group(0), m.group(1), m.group(2), m.groups())

t = '19:05:30'

# 贪婪匹配
# 正则表达式默认是贪婪匹配也就是匹配尽可能多的字符
m = re.match(r'^(\d+)(0*)$', '102300')
print(m.groups()) # 由于\d+采用贪婪匹配,直接把后面的0全部匹配了, 结果0*只能匹配空字符串了
# 必须让\d+采用非贪婪匹配(也就是尽可能少的匹配), 才能把后面的0匹配出来, 
# 加个?就可以让\d+采用非贪婪匹配
m = re.match(r'^(\d+?)(0*)$', '102300')
print(m.groups())

# 编译
# re模块内部会干两件事情
# 	1.编译正则表达式, 如果正则表达式的字符串本身不合法, 会报错;
# 	2.用编译后的正则表达式去匹配字符串.
# 如果一个正则表达式要重复使用几千次, 出于效率考虑, 我们可以预编译正则表达式
# 接下来重复使用时就不需要编译这个步骤了, 直接匹配
import re
# 编译:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

tz_str = 'UTC+7:00'
re_com = re.compile(r'^(\w{3})-(\d{3})$')
print(re_com.match('UTC-123').groups())
s = re.split(r'[\+\:]', tz_str)
print(s)
print(s[1])
