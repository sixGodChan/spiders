import redis

pool = redis.ConnectionPool(host='192.168.99.136', port=6379, password=123)
conn = redis.Redis(connection_pool=pool)
pb = conn.pubsub()  # 取值
pb.subscribe('fm104.5')

while True:
    msg = pb.parse_response()
    print(msg)
