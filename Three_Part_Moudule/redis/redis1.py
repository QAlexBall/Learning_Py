import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set('name', 'alex')
print(r['name'])
print(r.get('name')) # 取出键name对应的值
print(type(r.get('name')))
"""
output:
➜  redis git:(master) ✗ python redis1.py
alex
alex
<class 'str'>
"""