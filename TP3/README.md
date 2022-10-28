# BDA - TP3

## Une api simple géographique

2- la ville la moins peuplé : ce n'est pas possible

3- curl 'https://geo.api.gouv.fr/communes?nom=Mon&boost=population&limit=1'

4- curl https://geo.api.gouv.fr/departements/59/communes | jq > nord.json

## Installer CouchDB

1-  ip $couchdb = 172.28.100.246

3- changer le fichier de config `/opt/couchdb/etc/local.ini`:

    [chttpd]
    port = 5984
    bind_address = 0.0.0.0

4- la commande `curl 172.28.100.246:5984 | jq` retourne comme resultat :

```json
{
  "couchdb": "Welcome",
  "version": "3.2.2",
  "git_sha": "d5b746b7c",
  "uuid": "998a05a0ec2d727a3e61be5830991fb2",
  "features": [
    "access-ready",
    "partitioned",
    "pluggable-storage-engines",
    "reshard",
    "scheduler"
  ],
  "vendor": {
    "name": "The Apache Software Foundation"
  }
}
```

## Manipulation simple

- curl -u cha:admin -X PUT 172.28.100.246:5984/testing
- curl -u cha:admin -X DELETE 172.28.100.246:5984/testing
- curl -u cha:admin -X PUT --data '{"pain":["au", "chocolat"]}' 172.28.100.246:5984/testing/chouquette
{"ok":true,"id":"chouquette","rev":"1-ae190de59cdf3ff22b50a3fdee924c24"}

## Interaction programmatique

le code est dans le fichier [API.py](API.py) et le fichier [launcher.py](launcher.py)

## Recherche

