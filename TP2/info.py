import redis_connect
import os, json

# toute la ligne
cookie = os.environ.get("HTTP_COOKIE")
if(cookie is None):
    print("HTTP/1.1 400 Bad Request\n")
    print("No sessionId cookie")
    exit()
r5 = redis_connect.connection_redis(5)
# la value du cookie
cookie = cookie.split("=")[1]
if(not r5.exists(cookie)):
    print("HTTP/1.1 400 Bad Request\n")
    print( "sessionId cookie is invalid")
tmptoken = r5.get(cookie)
r5.expire(tmptoken, 60*10)
r2 = redis_connect.connection_redis(2)
print("HTTP/1.1 200 OK")
print("Content-Type: application/json\n")
print(json.dumps(
    {
        "username": r2.hget(tmptoken, "username").decode(), 
        "creationDate": r2.hget(tmptoken, "creationDate").decode(), 
        "lastConnection": r2.hget(tmptoken, "lastConnection").decode()
    }
))