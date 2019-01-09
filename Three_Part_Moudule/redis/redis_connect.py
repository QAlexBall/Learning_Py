import redis

# redis连接
host = 'localhost'
port = 6379
r = redis.Redis(host=host, port=port, decode_responses=True)
r.set('name', 'alex')
print(r['name'])
print(type(r.get('name')))