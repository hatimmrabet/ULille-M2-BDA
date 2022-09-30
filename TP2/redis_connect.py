import redis

def connection_redis(nbBase):
	r = redis.Redis(host="172.28.100.120", port=6379, password="univ-lille-BDA", db=nbBase)
	return r