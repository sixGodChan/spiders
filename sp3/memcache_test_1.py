import memcache

mc = memcache.Client(['192.168.11.60:12000'], debug=True)
ret = mc.get('foo')
print(ret)
