import redis

pool = redis.ConnectionPool(host='192.168.99.136', port=6379, password=123)

r = redis.Redis(connection_pool=pool)
r.set('foo', 'Bar')
print(r.get('foo'))
