import memcache

mc = memcache.Client(['192.168.11.60:12000'], debug=True)
mc.set("foo", 'bar1')
