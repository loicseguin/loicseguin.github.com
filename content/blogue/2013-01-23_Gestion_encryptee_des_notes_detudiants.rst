Gestion encryptée des notes d'étudiants
=======================================

:date: 2013/01/23
:author: Loïc Séguin-Charbonneau
:tags: enseignement, programmation
:status: draft

Depuis quelques temps, je gère les notes de mes étudiants à l'aide d'un petit
programme que j'ai créé, ``grades``.  Ce programme fonctionne en ligne de
commande et ne fait rien d'autre que de lire un fichier texte contenant les
notes et de calculer diverses moyennes et résultats cumulatifs.  Le fichier
texte contient un tableau au format reStructuredText_ ou org-mode_ que je
modifie avec mon éditeur de texte favori, vim_.  Pour obtenir les moyennes par
groupe et globale, je n'ai qu'à exécuter::

    grades print -m -g Groupe

et ``grades`` imprime un tableau contenant les notes des étudiants et les
moyennes de chacun des groupes de même que la moyenne de l'ensemble de
étudiants.  ``grades`` possède aussi quelques autres fonctionnalités utiles qui
sont expliquées dans la documentation.

Récemment, je me suis aperçu qu'il était très simple d'ajouter une protection
supplémentaire aux fichiers de note en les cryptant avec GnuPG.  J'ai dû
modifier légèrement ``grades`` pour qu'il puisse lire ces fichiers cryptés et
j'ai également ajouté une extension à ``vim`` pour ne pas devoir manuellement
décrypter et crypter les fichiers à chaque modification.


.. _reStructuredText: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
.. _org-mode: http://orgmode.org
.. _vim: http://www.vim.org
