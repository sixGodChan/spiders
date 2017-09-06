import redis

pool = redis.ConnectionPool(host='192.168.99.136', port=6379, password=123)
conn = redis.Redis(connection_pool=pool)
conn.publish('fm104.5', 'alex')  # 发布消息
