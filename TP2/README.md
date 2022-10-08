# BDA - TP2

## QUetsion 2:

l'adresse IP de la VM: 172.28.100.120

## Question 3:

Pour ceci, on commente la ligne `univ-lille-BDA`, puis on ajoute la ligne: `requirepass univ-lille-BDA` dans le fichier `redi/etc/redis/redis.conf` et on redémarre le serveur.

Mot de passe : univ-lille-BDA

Maintenat, on peut se connecter au serveur redis avec la commande

    redis-cli -h 172.28.100.120

et apres,

    auth univ-lille-BDA

## Question 4:

SELECT index : permet d'utiliser une base de données spécifique. On peut utiliser la commande `SELECT` pour changer de base de données.

Si on met SELECT 0, puis GET big_answer, on aura "42".


Pour tester le fonctionnement avec python , j'ai utiliser le fichier [test_python](test_python.py)

## Les intergiciels (ou middleware)

### Question 1:

$middleware_ip = 172.28.100.156

### Question 2:

    curl 172.28.100.156

### Question 3:

Pour activer cgi:

    sudo lighttpd-enable-mod
    cgi
    sudo service lighttpd force-reload

### Question 4:

    sudo nano hello.cgi


    C:\Users\hatim>curl 172.28.100.156/hello.cgi
    This is CGI!

### Question 5:

pour creer le fichier : 
    
    sudo nano env.cgi

La commande retourne le resultat suivant:

    C:\Users\hatim>curl 172.28.100.156/env.cgi
    SERVER_NAME=172.28.100.156
    SCRIPT_NAME=/env.cgi
    REDIRECT_STATUS=200
    GATEWAY_INTERFACE=CGI/1.1
    SERVER_SOFTWARE=lighttpd/1.4.63
    DOCUMENT_ROOT=/var/www/html
    PWD=/var/www/html
    REQUEST_URI=/env.cgi
    REQUEST_SCHEME=http
    QUERY_STRING=
    HTTP_ACCEPT=*/*
    REMOTE_PORT=51181
    HTTP_HOST=172.28.100.156
    SERVER_ADDR=172.28.100.156
    HTTP_USER_AGENT=curl/7.83.1
    SHLVL=1
    CONTENT_LENGTH=0
    SERVER_PROTOCOL=HTTP/1.1
    SERVER_PORT=80
    SCRIPT_FILENAME=/var/www/html/env.cgi
    REMOTE_ADDR=10.135.4.234
    REQUEST_METHOD=GET
    _=/usr/bin/printenv

la commande retourne des données sur la requetes passée par le client, comme le nom du serveur, le nom du script, le nom du document racine, le protocole utilisé, le nom du fichier script, l'adresse IP du client, la méthode de requete, etc.
Et elle ne retourne pas les vrai valeurs des variables d'environnement\dots

### Question 6:

la commande passée:

    curl --data "Holla Mundo!" 172.28.100.156/env.cgi?halloWelt

le resultat:

    C:\Users\hatim>    curl --data "Holla Mundo!" 172.28.100.156/env.cgi?halloWelt
    SERVER_NAME=172.28.100.156
    SCRIPT_NAME=/env.cgi
    REDIRECT_STATUS=200
    GATEWAY_INTERFACE=CGI/1.1
    SERVER_SOFTWARE=lighttpd/1.4.63
    DOCUMENT_ROOT=/var/www/html
    PWD=/var/www/html
    HTTP_CONTENT_LENGTH=12
    REQUEST_URI=/env.cgi?halloWelt
    REQUEST_SCHEME=http
    QUERY_STRING=halloWelt
    HTTP_ACCEPT=*/*
    REMOTE_PORT=51281
    HTTP_HOST=172.28.100.156
    SERVER_ADDR=172.28.100.156
    HTTP_USER_AGENT=curl/7.83.1
    SHLVL=1
    CONTENT_LENGTH=12
    SERVER_PROTOCOL=HTTP/1.1
    SERVER_PORT=80
    SCRIPT_FILENAME=/var/www/html/env.cgi
    REMOTE_ADDR=10.135.4.234
    CONTENT_TYPE=application/x-www-form-urlencoded
    REQUEST_METHOD=POST
    _=/usr/bin/printenv
    Holla Mundo!

## Réécriture d’URL

la requete suivante:

    curl 172.28.100.156/une/url/foireuse?avec=donnée

retourne :

    C:\Users\hatim>    curl 172.28.100.156/une/url/foireuse?avec=donnée
    SERVER_NAME=172.28.100.156
    SCRIPT_NAME=/env.cgi
    REDIRECT_STATUS=200
    GATEWAY_INTERFACE=CGI/1.1
    SERVER_SOFTWARE=lighttpd/1.4.63
    DOCUMENT_ROOT=/var/www/html
    PWD=/var/www/html
    REQUEST_URI=/une/url/foireuse?avec=donn�e
    REQUEST_SCHEME=http
    QUERY_STRING=
    HTTP_ACCEPT=*/*
    REMOTE_PORT=51335
    HTTP_HOST=172.28.100.156
    SERVER_ADDR=172.28.100.156
    HTTP_USER_AGENT=curl/7.83.1
    SHLVL=1
    CONTENT_LENGTH=0
    SERVER_PROTOCOL=HTTP/1.1
    SERVER_PORT=80
    SCRIPT_FILENAME=/var/www/html/env.cgi
    REMOTE_ADDR=10.135.4.234
    REDIRECT_URI=/env.cgi
    REQUEST_METHOD=GET
    _=/usr/bin/printenv

la variable REQUEST_URI contient l'URL initiale.

## CGI avec Python

### Question 4:

On a le resultat suivant. Qui est le resultat de l'execution du script python, et il affiche les variable de la requete passée.

    C:\Users\hatim>curl 172.28.100.156/env
    CONTENT_LENGTH:0
    QUERY_STRING:
    REQUEST_URI:/env
    REDIRECT_URI:/env.py
    REDIRECT_STATUS:200
    SCRIPT_NAME:/env.py
    SCRIPT_FILENAME:/var/www/html/env.py
    DOCUMENT_ROOT:/var/www/html
    REQUEST_METHOD:GET
    SERVER_PROTOCOL:HTTP/1.1
    SERVER_SOFTWARE:lighttpd/1.4.63
    GATEWAY_INTERFACE:CGI/1.1
    REQUEST_SCHEME:http
    SERVER_PORT:80
    SERVER_ADDR:172.28.100.156
    SERVER_NAME:172.28.100.156
    REMOTE_ADDR:10.135.4.234
    REMOTE_PORT:51392
    HTTP_HOST:172.28.100.156
    HTTP_USER_AGENT:curl/7.83.1
    HTTP_ACCEPT:*/*
    LC_CTYPE:C.UTF-8

# Un intergiciel et Redis pour une petit application web

## La création de compte

## Question 1:

1- le code se trouve dans le fichier [redis_connect](redis_connect.py), et on a utiliser l'ip_redis qu'on a fait dans les exercices precedants.

Pour ne pas l’exposer à l’extérieur, on modifie cette ligne dans le fichier `10-rewrite.conf`:

    url.rewrite-once = ( "redis_connect.py" => "/." )

2- Tout le code de la creation d'un compte se trouve dans le fichier [create.py](create.py).

on a testé avec la commade suivante, pour la creation d'un utilisateur Hatimo:

```sh
$ curl -v -X POST -d 'username=hatimo&password=testingg' 172.28.100.156/create

Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 172.28.100.156:80...
* Connected to 172.28.100.156 (172.28.100.156) port 80 (#0)
> POST /create HTTP/1.1
> Host: 172.28.100.156
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Length: 33
> Content-Type: application/x-www-form-urlencoded
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 201 Created
< Content-Length: 25
< Date: Thu, 06 Oct 2022 18:14:27 GMT
< Server: lighttpd/1.4.63
< 
User created succesfully
* Connection #0 to host 172.28.100.156 left intact
```
Et on recoit le code 201, qui signifie que la creation a été effectué avec succes.

## Connexion au compte

1- le fichier de routes contient:
```sh
url.rewrite-once = (
        "^/connect" => "/connect.py",
        "^/create" => "/create.py",
#       "redis_connect.py" => "/."      
)
```

2- Tout le code de la connexion d'un compte se trouve dans le fichier [connect.py](connect.py)

on a testé avec la commance suivante, et on a eu la reponse suivante pour un cas normale:

```sh
$ curl -v -X POST -d 'username=hatimo&password=testingg' 172.28.100.156/connect

Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 172.28.100.156:80...
* Connected to 172.28.100.156 (172.28.100.156) port 80 (#0)
> POST /connect HTTP/1.1
> Host: 172.28.100.156
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Length: 33
> Content-Type: application/x-www-form-urlencoded
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Set-Cookie: sessionId=1af8139a-634d-4a8f-996f-091c7265fddf; Max-Age=600
< Content-Length: 27
< Date: Thu, 06 Oct 2022 18:19:40 GMT
< Server: lighttpd/1.4.63
< 
User connected succesfully
* Connection #0 to host 172.28.100.156 left intact
```

et si on a un cas d'erreur, on a la reponse suivante (code 401, mot de passe incorrect):


```sh
$ curl -v -X POST -d 'username=hatimo&password=test' 172.28.100.156/connect

Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying 172.28.100.156:80...
* Connected to 172.28.100.156 (172.28.100.156) port 80 (#0)
> POST /connect HTTP/1.1
> Host: 172.28.100.156
> User-Agent: curl/7.81.0
> Accept: */*
> Content-Length: 29
> Content-Type: application/x-www-form-urlencoded
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 401 Unauthorized
< Content-Length: 15
< Date: Thu, 06 Oct 2022 18:53:48 GMT
< Server: lighttpd/1.4.63
< 
Wrong password
* Connection #0 to host 172.28.100.156 left intact
```


## Avoir des informations sur le compte

1- le fichier contient les routes suivantes:

```sh
 url.rewrite-once = (
        "^/env" => "/env.py",
        "^/connect" => "/connect.py",
        "^/create" => "/create.py",
        "^/" => "/info.py",
)
```

2- le code se trouve dans le fichier [info.py](info.py), pour tester:

- si on a pas de cookie: Ona la reponse 400 avec le message (No sessionId cookie)

```sh
$ curl -v  172.28.100.156/

*   Trying 172.28.100.156:80...
* Connected to 172.28.100.156 (172.28.100.156) port 80 (#0)
> GET / HTTP/1.1
> Host: 172.28.100.156
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 400 Bad Request
< Content-Length: 20
< Date: Thu, 06 Oct 2022 19:00:09 GMT
< Server: lighttpd/1.4.63
< 
No sessionId cookie
* Connection #0 to host 172.28.100.156 left intact
```
- si on a un cookie, on a la reponse 200, et les informations sous format json.

```sh
$ curl -v --cookie "HTTP_COOKIE=a1af8139a-634d-4a8f-996f-091c7265fddf" 172.28.100.156/

*   Trying 172.28.100.156:80...
* Connected to 172.28.100.156 (172.28.100.156) port 80 (#0)
> GET / HTTP/1.1
> Host: 172.28.100.156
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Content-Type: application/json
< Accept-Ranges: bytes
< Content-Length: 103
< Date: Thu, 06 Oct 2022 19:25:24 GMT
< Server: lighttpd/1.4.63
< 
{"username": "hatimo", "creationDate": "06-10-2022 18:14:27", "lastConnection": "06-10-2022 19:19:43"}
* Connection #0 to host 172.28.100.156 left intact
```

## API d’upload et de download de fichier

le fichier devient:
    
```sh
url.rewrite-once = (
    "^/test" => "/create.py",
    "^/env" => "/env.py",
    "^/connect" => "/connect.py",
    "^/create" => "/create.py",
    "^/files/" => "gestion_fichier.py",
    "^/" => "/info.py",
    "^/redis_connect.py" => "/."    
)
```