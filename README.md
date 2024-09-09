PdfCleanner
============

### PRÉSENTATION

Cet outils a pour but d'effectuer des modification sur des pdf sans les stocker ni en base de donner ni sur le disque du serveur.

Pour atteindre cet objectif , ce programme utilise les modules Pypdf ( pour la manipulation des pdf ) et ByteIO ( pour manipuler les fichier sans les stocker sur le disque) et tous ça en version grâce au framework Django.

Pour le moment l'outil ne sers qu'à supprimer le texte dans un pdf pour créer un template de l'original . Cependant le programme integrera certainemt plus de fonctionnalité a l'avenir

### TÉLÉCHARGEMENT

Comme tous les projets sur github vous pouvez le télécharger en le clonant :


´´´
$ git clone ...

$ pip install Pypdf

$ pip install django
´´´


### UTILISATION

Il suffit de se rendre dans le dossier pdfcleaner/pdfcleanner , puis de lancer le serveur en utilisant la l'instruction suivant :

´´´bash
$ ./manage.py runserver
´´´
Et de se rendre sur le lien indiquer, puis entrer le titre du fichier et sélectionner le fichier pdf . Dès que vous validez le formulaire le template du fichier pdf est automatiquement télécharger
