# Projet BDA

## Introduction:

### Contexte:

La mission dans laquelle Hatim et moi avons été affecté consiste à l’automatisation/remédiation de service sur les serveur de nos clients. Le processus d’automatisation/auto-remédiation se fait à l’aide de sondes qui “surveillent” les services. Lorsqu’un sonde est déclenchée, elle alerte la plateforme AWX qui va en fonction de la sonde, exécuter l’automate correspondant afin de régler le problème. Le dashboard d’AWX ne satisfaisant pas les envies de l’équipe, nous nous sommes proposé afin d’en produire un avec les attentes de chacun. Le projet étant assez complexe, il sera réalisé tout au long de notre contrat chez Inetum afin d’apporter une amélioration continue.

### Problématique:

L’objectif est de solliciter l’api d’AWX afin de récupérer toutes les informations nécessaires, les stocker ainsi que les afficher de façon compréhensibles. Nous nous sommes donc demandés comment automatiser la récupération de données à l’aide d’un playbook Ansible et rendre ces informations disponibles sur une application web ? 

Nous allons donc voir quelles technologies nous avons utilisé et pourquoi, la problématique concernant la confidentialité des bases de données des clients, les différentes solutions ainsi que sa mise en place et pour finir les limites de notre solution.

## Choix des technologies

Nous avons voulu découvrir de nouvelles technologies et c’est pour cela que nous nous sommes tournés vers GraphQL qui nous permettait de requêter d’une manière differente qu’avec une API REST, associé avec Hasura, nous gagnons du temps car la partie développement de l’API est automatiquement prise en charge par la solution. Cela nous a permit lors de notre requetage de ne demander que les champs dont nous avions besoin et donc de ne pas avoir à créer des endpoints et des requêtes personnalisés pour les différents éléments voulus.

![docs/schema.svg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/33b6fe42-5c48-45b4-8c4a-6d96b53bc4f3/schema.svg)

GraphQL un langage de requêtes et un environnement d'exécution. La particularité de GraphQL est que la structure de la réponse du serveur est fixée par le client.

Comme l’exemple qu’on a en haut, le code présent à coté du logo de GraphQL, présente une requête qui va recuperer les champs “id” et “name” de la table “profile”, avec un champs Authorization en cas de besoin.

Hasura est un moteur GraphQL open source qui permet de déployer des API GraphQL instantanées et en temps réel sur n’importe quelle base de données Postgres. Ce qui nous a permis dans notre projet de recuperer des données à partir de notre base de données postgres rapidement en prenant en compte le nombre de données qu’on a.