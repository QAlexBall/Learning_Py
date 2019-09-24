import redis

host = 'localhost'
port = 6379
pool = redis.ConnectionPool(host=host, port=port, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('gender', 'male')
print(r.get('gender'))
