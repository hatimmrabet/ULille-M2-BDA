import redis_connect
import datetime as dt
import hashlib as hl
import requests as req


def info():
    print(req.get_cookie("sessionId"))
    if(req.get_cookie("sessionId") is None):
        return "No sessionId cookie"
    r5 = redis_connect.connection_redis(5)
    if(not r5.exists(req.get_cookie("sessionId"))):
        return "sessionId cookie is invalid"
    tmptoken = r5.get(req.get_cookie("sessionId"))
    r5.expire(tmptoken, 60*10)
    req.headers["content-type"] = "application/json charset=utf-8"
    r2 = redis_connect.connection_redis(2)
    return r2.hgetall(r5.get(tmptoken))

info()
    