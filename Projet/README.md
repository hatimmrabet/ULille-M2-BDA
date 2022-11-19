# Projet BDA

## Introduction:

### Contexte:

La mission dans laquelle Hatim et moi avons été affecté consiste à l’automatisation/remédiation de service sur les serveur de nos clients. Le processus d’automatisation/auto-remédiation se fait à l’aide de sondes qui “surveillent” les services. Lorsqu’un sonde est déclenchée, elle alerte la plateforme AWX qui va en fonction de la sonde, exécuter l’automate correspondant afin de régler le problème. Le dashboard d’AWX ne satisfaisant pas les envies de l’équipe, nous nous sommes proposé afin d’en produire un avec les attentes de chacun. Le projet étant assez complexe, il sera réalisé tout au long de notre contrat chez Inetum afin d’apporter une amélioration continue.

### Problématique:

L’objectif est de solliciter l’api d’AWX afin de récupérer toutes les informations nécessaires, les stocker ainsi que les afficher de façon compréhensibles. Nous nous sommes donc demandés comment automatiser la récupération de données à l’aide d’un playbook Ansible et rendre ces informations disponibles sur une application web ? 

Nous allons donc voir quelles technologies nous avons utilisé et pourquoi, la problématique concernant la confidentialité des bases de données des clients, les différentes solutions ainsi que sa mise en place et pour finir les limites de notre solution.