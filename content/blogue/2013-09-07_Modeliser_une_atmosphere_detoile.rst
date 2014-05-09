Modéliser une atmosphère d'étoile
=================================

:date: 2013-09-07
:author: Loïc Séguin-Charbonneau
:tags: physique
:status: draft

Lorsqu'on observe une étoile, ce qu'on voit est la lumière qui a été émise à
différentes profondeurs dans l'étoile et qui a été modifiée par son passage à
travers les couches moins profondes de l'étoile.  Cette lumière transporte de
l'information sur la composition chimique, la température et la pression à
toutes les profondeurs de l'étoile.  Pour bien comprendre cette information, il
faut savoir comment la lumière est affectée par son passage à travers le gaz
qui constitue l'étoile.

La situation est analogue à celle où on place une ampoule au tungstène derrière
un verre d'eau et qu'on mesure la lumière reçue à travers le verre d'eau.  Les
caractéristiques de cette lumière dépendent de la source, sa température, sa
composition chimique, mais aussi de l'eau à travers laquelle elle est passée.
Les caractéristiques de la source ne peuvent être bien comprises que si on a un
bon modèle de la façon avec laquelle l'eau modifie les propriétés de la lumière
qui la traverse.


Qu'est-ce qu'une étoile?
------------------------

Prenons d'abord le Soleil comme exemple.  Le Soleil est une boule de gaz très
chaud qui est maintenue en une forme à peu près sphérique grâce à la force de
gravité.  La pression de ce gaz augmente avec la profondeur de la même façon
que la pression augmente avec la profondeur dans les océans sur Terre.  Étant
donné qu'il y a une relation entre la pression et la température, qu'on appelle
une équation d'état, la température augmente elle aussi avec la profondeur.
Une équation d'état bien connue est celle du gaz parfait

.. math::
    P = nkT

où :math:`P` est la pression, :math:`V` est le volume, :math:`n` est la densité
en terme du nombre de particules par unité de volume, :math:`k` est la
constante de Boltzmann, et :math:`T` est la température.  Si cette équation
d'état décrivait le gaz qui forme le Soleil (ce n'est pas le cas), alors on
voit qu'une augmentation de pression a tendance à provoquer une augmentation de
la température.

La pression et la température au centre du Soleil sont suffisamment élevées
pour que les atomes d'hydrogène entrent en collision et fusionnent pour donner
de l'hélium (le processus exact est plus complexe).  Cette réaction de fusion
libère de grandes quantités d'énergie sous forme de radiation électromagnétique,
c'est-à-dire de la lumière, incluant des rayons UV, X et gamma.  Cette
radiation, de même que celle qu'émet le gaz chaud lui-même, tente de s'échapper
vers la surface.  Pourquoi?  Lorsqu'elle interagit avec des particules, par
exemples les atomes qui forment le gaz, la lumière se comporte comme une
particule qu'on appelle un photon.  Ce photon voyage en ligne droite jusqu'à ce
qu'il heurte une particule ce qui fait dévier sa trajectoire dans une direction
aléatoire.  Étant donné la grande concentration d'atomes au coeur du Soleil, le
nombre de collision est élevé et le photon rebondi plusieurs fois dans des
directions aléatoires.  Ce comportement peut être représenté par une marche
aléatoire en trois dimensions, un outil mathématique à partir duquel il est
possible de démontrer que le photon ne reviendra qu'un nombre fini de fois à
son point de départ.  Il est donc condamné à éventuellement s'éloigner de son
point de départ et à ne jamais y revenir, autrement dit, le photon s'échappe
vers l'extérieur de l'étoile.

Le mouvement de tous ces photons qui se dirigent vers l'extérieur crée une
pression vers l'extérieur.  Cette pression, combinée avec la pression thermique
due au mouvement aléatoires des atomes eux-mêmes est ce qui empêche l'étoile de
s'écrouler sous sa propre gravité.




