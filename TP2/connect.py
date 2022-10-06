import sys, os
from redis_connect import connection_redis
import uuid
import datetime as dt
import hashlib as hl


form = sys.stdin.readline()
if(form is None or len(form)==0):
	print("HTTP/1.1 400 Bad Request\n")
	print("Form is empty")
	exit()
fields = form.split("&")
if(len(fields) != 2):
	print("HTTP/1.1 400 Bad Request\n")
	print("Form is invalid")
	exit()
username = fields[0].split("=")[1]
password = fields[1].split("=")[1]
if(username is None or len(username)==0 or password is None or len(password)==0):
	print("HTTP/1.1 400 Bad Request\n")
	print("Username or password is empty")
	exit()
r = connection_redis(1)
if(not r.exists(username)):
	print("HTTP/1.1 400 Bad Request\n")
	print("Username doesn't exist")
	exit()
tokenid = r.get(username)
r2 = connection_redis(2)
if(str(r2.hget(tokenid, "password").decode()) != hl.sha256(password.encode()).hexdigest()):
	print("HTTP/1.1 401 Unauthorized\n")
	print("Wrong password")
	exit()
tmpuuid = str(uuid.uuid4())
r5 = connection_redis(5)
r5.set(tmpuuid, tokenid)
r5.expire(tmpuuid, 60*10)
r2.hset(tokenid, "lastConnection", dt.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
print("HTTP/1.1 200 OK")
os.environ["HTTP_COOKIE"] = tmpuuid
print("Set-Cookie: sessionId="+tmpuuid+"; Max-Age=600\n")
print("User connected succesfully")