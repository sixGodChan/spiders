import redis

pool = redis.ConnectionPool(host='192.168.99.136', port=6379, password=123)

r = redis.Redis(connection_pool=pool)

# 事务
# pipe = r.pipeline(transaction=True)
# pipe.set('foo', 'Bar')
# pipe.set('role', 'actor')
# pipe.execute()

r.set('foo', 'Bar')
print(r.get('foo'))
