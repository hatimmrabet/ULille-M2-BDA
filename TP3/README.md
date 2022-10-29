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

## Recherche et Indexes

Pour avoir la ville la moins peuplées de la région Auvergne-Rhones-Alpes, on a creer une fonction qui à partir du données de la table "france" cherche les ville avec le codeRegion = 84 (celui de la region Auvergne-Rhones-Alpes) et puis les ranger par ordre croissant de population et retourner la premiere ville.

Pour les ordonnées on a du ajouter un index sur le champs "population" de la table "france" avec la fonction `createIndexOnField`, et on obtient le resultat suivant :

```bash
{
  "docs": [
    {
      "_id": "5fff04e1055182640f333642b01d935e",
      "_rev": "1-b58189968dbf2646bf313352f56f39b7",
      "nom": "Rochefourchat",
      "code": "26274",
      "codeDepartement": "26",
      "siren": "212602742",
      "codeEpci": "242600534",
      "codeRegion": "84",
      "codesPostaux": [
        "26340"
      ],
      "population": 1
    }
  ],
  "bookmark": "g2wAAAACaAJkAA5zdGFydGtleV9kb2NpZG0AAAAgNWZmZjA0ZTEwNTUxODI2NDBmMzMzNjQyYjAxZDkzNWVoAmQACHN0YXJ0a2V5awABAWo",
  "execution_stats": {
    "total_keys_examined": 0,
    "total_docs_examined": 0,
    "total_quorum_docs_examined": 0,
    "results_returned": 1,
    "execution_time_ms": 23.89
  }
}
```

Pour recuperer la ville la plus peuplée commenceant par "Mon", on a creer une fonction qui à partir du données de la table "france" cherche les ville avec le nom commence par "Mon" et puis les ranger par ordre decroissant de population et retourner la premiere ville.

```bash
{
  "docs": [
    {
      "_id": "5fff04e1055182640f333642b0933576",
      "_rev": "1-4bcae2bf3aeb35bc2a5ebb42ce42fc9a",
      "nom": "Montpellier",
      "code": "34172",
      "codeDepartement": "34",
      "siren": "213401722",
      "codeEpci": "243400017",
      "codeRegion": "76",
      "codesPostaux": [
        "34070",
        "34000",
        "34090",
        "34080"
      ],
      "population": 295542
    }
  ],
  "bookmark": "g2wAAAACaAJkAA5zdGFydGtleV9kb2NpZG0AAAAgNWZmZjA0ZTEwNTUxODI2NDBmMzMzNjQyYjA5MzM1NzZoAmQACHN0YXJ0a2V5bAAAAAFiAASCdmpq",
  "execution_stats": {
    "total_keys_examined": 0,
    "total_docs_examined": 0,
    "total_quorum_docs_examined": 0,
    "results_returned": 1,
    "execution_time_ms": 174.356
  }
}
```

On remarque que on utilisant les index, on a pas besoin de parcourir toute la table, on a juste besoin de parcourir les index et on obtient le resultat en un temps tres court.