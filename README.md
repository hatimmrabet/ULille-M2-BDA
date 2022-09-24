# BDA

## Les adresses IP:

- ubuntu: ubuntu@172.28.100.16 (password: 123456)
- hatimmrabet: hatimmrabet@172.28.100.16 (password: 123456)

### Question 7

Creation du compte cha sur postgres, on se connecte avec ubuntu, apres, on se connecte avec postgre avec la commande `sudo su postgres` :

```bash
psql
\password cha
```
sur openstack, on cree la base de donnees ``create database microblog;``

sur la machine virtuelle, on lance la commande ``cat ./Bureau/microblog.sql | psql -h 172.28.100.16 -U hatimmrabet --dbname microblog``

### Question 8

- On charge une extension pour le generation des uuid et une autre pour le cryptage des mots de passe
- la table user_store contient les informations des utilisateurs, avec une cle primaire user_id generer automatiquement avec l'exetention qu'on vient de charger, et on met un index sur le nom de l'utilisateur.
- la fonction create_user permet de creeer un utilisateur en crypton le mot de passe avec l'extension pgcrypto, et on retourne l'uuid de l'utilisateur cree.
- la table messages_store contient les messages, avec une cle primaire message_id generer automatiquement avec la fonction uuid_generate_v1. et on a une cle etranger user_id qui fait reference a la table user_store. Et ajoute un index sur sur la date de publication d'un message. on a un cluster qui organise la table par date de publication.
- une fonction pour l'insertion des messages dans la table, en recuperant le user_id a partir de son nom et mot de passe passées en parametres, et on ajoute le contenue et l'user_id de la personne à qui on a repondu, pour la preparation de la requete de l'insertion.
- On a une vue qui prend les 30 derniers messages publiés.
- la tables followers permet d'avoir qui suit qui, en etant sur qu'on peut pas se suivre soi meme, et on ne peut pas suivre deux fois la meme personne. On a aussi un index sur le couple (follower_id, followed_id).
- la fonction feed, permet d'avoir la liste des messgaes des personnes que l'on suit, et on trie par date de publication, en utilisant le nom et mot de passe de la personne connecté.
- certain fonction sont securisé et ne peuvent etre que par un utilisateur avec un role autorisé.
- la fonction follow, permet d'inserer dans la table followers.
- et à la fin, on supprime le role common_user, et on le reecree avec le droit LOGIN pour pouvoir se connecter. et on permet l'execution des fonctions create_user, insert_message, feed et follow pour tous les utilisateurs avec le role common_user. et aussi on leur permet de lire à partir la view messages.

### Question 9
- non, il a droit de voir que les 30 derniers messages.
- non.
- non.
L’utilisateur possédant la base de données peut tout faire sauf que le mot de pase recupéré est crypté, donc il ne peut pas le lire.

### Question 10

Reordonner physiquemment la table messages_store par date de publication.

### Question 12
j'ai mis cette ligne avant la ligne qui permet la connection de tout le monde
host | all | common_user | 0.0.0.0/0 | trust

### Question 13

Le code du Bot est dans le fichier [BlogBot.py](BlogBot.py), il permet de publier des messages aleatoires, et de repondre aux messages des autres utilisateurs.
ainsi qu'il follow tous les utilisateur qui ont deja repondu à son message. Les utilisateur qui repondent à un message ont 50% de chance pour suivre celui qui a posté ce message.

### Question 14

1 process, 500 utilisateurs, max TPS 18.
2 process, 500 utilisateurs chacune, max TPS 25.
6 process, 500 utilisateurs chacune, max TPS 63, total queries 1443, total time 352s.
16 process, 100 utilisateurs chacune, max TPS 111.
24 process, 100 utilisateurs chacune, max TPS 126.
32 process, 100 utilisateurs chacune, max TPS 168.