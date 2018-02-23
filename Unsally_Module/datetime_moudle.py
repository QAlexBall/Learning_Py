# datetime是Python处理日期和时间的标准库

# 获取当前的日期和时间
from datetime import datetime
now = datetime.now() # 获取当前datetime
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)

# datetime转换为timestamp
# 1970-1-1 00:00:00 UTC+00:00失去的时刻称为epoch time, 记为0
# 之前的timestamp为负数, 当前时间就是相对于epoch time的秒数, 称为timestamp
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# 对应的北京时间是
# timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
dt = datetime(2015, 1, 20, 12, 00)
print(dt.timestamp())

# timestamp转换为datetime
t = 1432428043.0
print(datetime.fromtimestamp(t)) # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间

# str转换为datetime
# 很多时候用户输入的时间和日期是字符串, 要处理时间和日期, 首先必须把str转换为datetime, 
# 转换方法是通过datetime.strptime()实现, 需要一个时间和日期的格式化字符串

cday = datetime.strptime('2015-9-3 19:39:34', '%Y-%m-%d %H:%M:%S')
print(cday) # 转换后的datetime是没有时区信息的

# datetime转换为str
# 如果有了datetime对象, 要把它格式化为字符串显示给用户, 就需要转换为str

from datetime import datetime, timedelta
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
now = datetime.now()
print(now)
now = now + timedelta(hours=10)
print(now)
now = now - timedelta(hours=10)
print(now)

# 本地时间转换为UTC时间
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8))# 创建时区UTC+8:00
now = datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)

# 时区转换
# 通过utcnow()拿到当前的UTC时间, 再转换为任意时区的时间
print()
# 拿到UTC时间, 并强制转换为任意时区的时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
#astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo2_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo2_dt)

# datetime表示的时区信息才能确定一个特定的时间, 否则只能视为本地时间
# 如果存储datetime, 最佳方法是将其转换为timestamp再存储, 因为timestamp的值与时区完全无关

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
	dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')	
	tz_str_2_int = re.split(r'[\+\:]', tz_str)
	utc_dt = dt.astimezone(timezone(timedelta(hours=int(tz_str_2_int[1]))))
	print('timezone:',   tz_str_2_int[1])
	result = utc_dt.timestamp()
	return result

t1 = to_timestamp('2019-1-1 08:00:00', 'UTC+7:00')
print(t1)
print(datetime.fromtimestamp(t1))
assert t1 == 1546300800.0, t1
print('Pass')