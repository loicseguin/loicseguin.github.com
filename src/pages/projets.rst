Projets
=======

À moins d'une mention contraire, tous les projets libres sur lesquels je
travaille sont distribués sous une licence BSD.


NetworkX
--------

http://networkx.lanl.gov/

**NetworkX** est une librairie *Python* pour manipuler des graphes. En plus de
classes pour différents types de graphes (orienté ou non, graphe simple ou
multi-graphe), la librairie contient un grand nombre de générateurs de graphes
et une vaste banque d'algorithmes (plus courts chemins, connectivité, arbres de
recouvrement, isomorphismes, flots, etc.).

Le projet est une initiative d'un petit groupe de chercheurs du *Los Alamos
National Laboratory* qui ont débuté son développement il y a près d'une dizaine
d'années. La librairie est stable et performante et permet de se lancer dans la
résolution de problèmes liés aux graphes sans difficulté.

Je me suis joint au projet en 2010. Mes contributions principales ont été de
convertir le code pour qu'il soit compatible avec la version 3 de Python et de
créer le paquetage des algorithmes de flots. Depuis environ un an, je m'occupe
surtout de maintenir ce même paquetage.


Grades
------

https://github.com/loicseguin/grades/

Après m'être battu contre Excel et Numbers, je me suis converti à l'utilisation
d'un fichier texte pour comptabiliser les notes de mes étudiants. Évidemment,
un fichier texte n'offre pas la possibilité de faire des calculs. **Grades**
est un programme écrit en *Python* qui s'occupe de lire un fichier de notes et
de calculer les moyennes et les notes cumulatives. Pour l'instant, le fichier
texte doit contenir un tableau qui respecte le format des tableaux de
org-mode_. J'ai l'intention d'ajouter d'autres formats de tableaux (rst, csv)
éventuellement.

.. _org-mode: http://orgmode.org/


Mathoscope
----------

https://github.com/loicseguin/mathoscope/
https://mathoscope.herokuapp.com/

**Mathoscope** est une application web écrite avec *Ruby on Rails*. Cette
application permet à des étudiants de tester leurs connaissances en répondant à
des questions à choix multiples ou a réponse courte. Le professeur possède un
accès d'administrateur qui lui permet d'ajouter des questions et de suivre
la progression des étudiants.


Spinify
-------

https://bitbucket.org/loicseguin/spinify/

**Spinify** est un logiciel de simulation du modèle d'Ising sur différentes
surfaces. Le logiciel utilise un algorithme de Monte Carlo basé sur une chaîne
de Markov pour mesurer les propriétés physiques (énergie, magnétisation,
fonction de corrélation) d'un réseau dans lequel chaque noeud possède un spin
up ou un spin down. L'utilisateur peut spécifier un réseau classique (carré,
triangulaire) ou un réseau aléatoire (sur le tore plat ou sur la sphère).
