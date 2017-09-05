# import redis
#
# r = redis.Redis(host='192.168.11.60', port=6379)
# r.set('foo', 'bar')
# print(r.get('foo'))

import redis

r = redis.Redis(host='192.168.99.136', port=6379, password=123)
r.set('foo', 'Bar')
print(r.get('foo'))
