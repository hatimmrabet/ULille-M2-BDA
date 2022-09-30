import hashlib as hl
import datetime as dt
import uuid
import sys
from redis_connect import connection_redis

def create():
	form = sys.stdin.readline()
	if(form is None or len(form)==0):
		return("Form is empty")
	fields = form.split("&")
	if(len(fields) != 2):
		return("Form is invalid")
	username = fields[0].split("=")[1]
	password = fields[1].split("=")[1]
	if(username is None or len(username)==0 or password is None or len(password)==0):
		return("Username or password is empty")
	r = connection_redis(1)
	if(r.exists(username)):
		return("Username already exists")
	password = hl.sha256(password.encode()).hexdigest()
	tokenid = str(uuid.uuid4())
	r.set(username, tokenid)
	r2 = connection_redis(2)
	r2.hset(tokenid, "username", username)
	r2.hset(tokenid, "password", password)
	r2.hset(tokenid, "creationDate", dt.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
	r2.hset(tokenid, "lastConnection", dt.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
	return( "User created")

print(create())