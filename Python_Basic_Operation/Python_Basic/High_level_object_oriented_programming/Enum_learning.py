from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
					'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
	print(name, '=>', member, ':', member.value) # value属性是自动赋给成员的int常量, 默认从1开始计数
# 如果需要更精确地控制枚举类型, 可以从Enum派生出自定义类
from enum import Enum, unique

@unique # unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
	Sun = 0 # Sun的value值被设置为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6
day1 = Weekday.Mon
print(day1, day1.value, Weekday(6))
# Weekday(7) output: ValueError: 7 is not a valid Weekday
print(Weekday.Mon, Weekday['Mon'], day1 == Weekday['Mon'], day1 == Weekday(1))

