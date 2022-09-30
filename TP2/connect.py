import sys
from redis_connect import connection_redis
import uuid
import datetime as dt
import hashlib as hl
import requests as req


def connect():
	form = sys.stdin.readline()
	if(form is None or len(form)==0):
		return "Form is empty"
	fields = form.split("&")
	if(len(fields) != 2):
		return "Form is invalid"
	username = fields[0].split("=")[1]
	password = fields[1].split("=")[1]
	if(username is None or len(username)==0 or password is None or len(password)==0):
		return "Username or password is empty"
	r = connection_redis(1)
	if(not r.exists(username)):
		return "Username doesn't exist"
	tokenid = r.get(username)
	r2 = connection_redis(2)
	if(str(r2.hget(tokenid, "password").decode()) != hl.sha256(password.encode()).hexdigest()):
		return "Wrong password"
	tmpuuid = str(uuid.uuid4())
	r5 = connection_redis(5)
	r5.set(tmpuuid, tokenid)
	r5.expire(tmpuuid, 60*10)
	r2.hset(tokenid, "lastConnection", dt.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
	return "Set-Cookie: sessionId="+tmpuuid+"; Max-Age=600"
	
print(connect())