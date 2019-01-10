import redis
import time
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('food', 'beef', px=3)
# print(r.get('food'))

# time.sleep(3)
# print(r.get('food'))
'''
➜  redis git:(master) ✗ python redis3.py
beef
None    # 三秒之后键food的值变成None
'''
r.set('food', 'beef', px=3)
print(r.get('food'))
time.sleep(0.3)
print(r.get('food')) # 三毫秒后键food的值变为None

print(r.set('fruit', 'watermelon', nx=True)) # nx=True只有name不存在时,当前set操作才执行
print(r.get('fruit'))

print(r.set('fruit', 'banana', xx=True)) # True fruit存在
print(r.set('fruit1', 'banana', xx=True)) # None fruit1不存在

print(r.setnx('fruit1', 'banana')) # fruit1不存在,输出位True
print(r.get('fruit1'))

