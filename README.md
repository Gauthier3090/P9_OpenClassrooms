# Développez une application Web en utilisant Django

![](https://camo.githubusercontent.com/7c691d06ed3e830244e052e43bb63780a25f0be9c7446cd4bea9f638dae92c99/68747470733a2f2f6f6e617465737465706f7572746f692e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032302f30322f4c6f676f5f6f70656e636c617373726f6f6d735f6f6e617465737465706f7572746f692e6a7067)

# Résumé du projet

Développer une application qui permette de demander ou de publier des critiques de livres ou d’articles.

## Connexion
Un utilisateur doit être connecté pour accéder aux services de LitReview.

S'il ne possède pas encore de compte, l'utilisateur est invité à créer un nouveau compte dès la page d'accueil.

Une fois connecté, l'utilisateur visualise le flux des demandes et des critiques qu'il a lui-même créées ainsi que celles d'autres membres qu'il a décidé de suivre.

## Abonnements
Afin de suivre un membre, l'utilisateur se rend sur la page "Abonnements". Sur cette page, l'utilisateur peut :

- S'abonner en sélectionnant dans la liste un membre qu'il souhaite suivre.
- Visualiser la liste des membres qui le suivent
- Visualiser la liste de ses abonnements et éventuellement s'y désabonner.
- L'utilisateur ne peut s'abonner à lui-même.

## Flux et Posts
La page du Flux permet à l'utilisateur de consulter l'ensemble des demandes et des critiques de ses abonnements ou de lui-même. A partir de la page du flux principal, l'utilisateur peut également créer une nouvelle demande ou rédiger une critique.

La page des Posts permet à l'utilisateur de consulter l'ensemble de ses demandes et critiques. Il peut alors les modifier ou les supprimer. Cependant, il ne peut supprimer une demande tant qu'il existe une critique qui y est rattachée.

# Configurer un environnement virtuel Python et lancer le projet Django

## Windows

La création d'environnements virtuels est faite en exécutant la commande venv :

````Bash
python -m venv \path\to\new\virtual\venv
````

Pour commencer à utiliser l’environnement virtuel, il doit être activé :

````Bash
.\venv\Scripts\activate.bat
````

Pour lancer le projet Django:

````Bash
cd .\src
py .\manage.py runserver
````

## Unix

La création d'environnements virtuels est faite en exécutant la commande venv :

````Bash
python3 -m venv \path\to\new\virtual\venv
````

Pour commencer à utiliser l’environnement virtuel, il doit être activé :

````Bash
source venv/bin/activate
````

Pour lancer le projet Django:

````Bash
cd .\src
python3 .\manage.py runserver
````
