import hashlib as hl
import datetime as dt
import uuid
import sys
from redis_connect import connection_redis

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
if(r.exists(username)):
	print("HTTP/1.1 400 Bad Request\n")
	print("Username already exists")
	exit()
password = hl.sha256(password.encode()).hexdigest()
tokenid = str(uuid.uuid4())
r.set(username, tokenid)
r2 = connection_redis(2)
r2.hset(tokenid, "username", username)
r2.hset(tokenid, "password", password)
r2.hset(tokenid, "creationDate", dt.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
r2.hset(tokenid, "lastConnection", dt.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
print("HTTP/1.1 201 created\n")
print("User created succesfully")