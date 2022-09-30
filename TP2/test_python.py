import redis

r = redis.Redis(host="172.28.100.120", port=6379, password="univ-lille-BDA", db=0) # changer l'addresse ip et le mot de passe
r["test_python"] = 42