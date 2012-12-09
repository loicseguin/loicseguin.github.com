Spinify
#######
:date: 2010-01-25 16:41
:tags: informatique, maths, physique
:summary:

Il y a quelques années, j'ai travaillé sur un projet qui consistait à
développer un programme de simulation du modèle d'Ising sur des surfaces
ayant un tenseur métrique non trivial. Ce projet n'a jamais été
complété. Or, je m'y suis récemment remis, et j'avance à bon train.
J'ai réécrit le code en C++ et j'ai implémenté un algorithme pour
générer un réseau aléatoire sur la sphère. Actuellement, j'utilise
`Qhull`_ pour essayer de trianguler le réseau ainsi obtenu, mais le code
est mal écrit et le programme plante souvent. Je travaille régulièrement
sur le projet, et si le coeur vous en dit, j'apprécierais avoir un peu
d'aide. Le code source pour le programme est disponible sur bitbucket à
l'adresse `http://bitbucket.org/loicseguin/spinify/`_.
Si ce qui précède est du pur charabia, ne vous en faites pas : avant
longtemps, j'écrirai un message détaillant ce qu'est le modèle d'Ising,
ce que j'entends par métrique non triviale et comment le programme
Spinify essaie de gérer tout cela.
|image0|

.. _Qhull: http://www.qhull.org/
.. _`http://bitbucket.org/loicseguin/spinify/`: http://bitbucket.org/loicseguin/spinify/

.. |image0| image:: https://blogger.googleusercontent.com/tracker/697344570467959391-7860750195897093739?l=mathfou.blogspot.com
