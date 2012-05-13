La programmation en nombres entiers.
####################################
:date: 2008-03-21 06:23
:tags: recherche opérationnelle, maths

Qu'est-ce qui fait de la programmation en nombres entiers un sujet
intéressant ? Pourquoi une poignée de mathématiciens dépensent-ils
quelques milliers de dollars pour se réunir et en discuter ? Sans doute
en saurais-je un peu plus à mon retour de la session de travail sur la
programmation en nombres entiers qui se tient dans une semaine à la
Barbade.

D'ici là, voici ce que j'en sais pour vous mettre l'eau à la bouche.
Tout d'abord, la programmation en nombres entiers (PNE) est une
sous-catégorie de problèmes de la programmation linéaire (PL). En PL, on
veut résoudre des problèmes d'optimisation du genre :
minimiser f(x)
sous les contraintes c_i (x) = 0 pour i dans E
c_i (x) <= 0 pour i dans I où E et I sont des ensembles d'indices, les
c_i et f sont des fonctions linéaires. En PNE, on rajoute la contrainte
que la solution doit être entière. Parfois, on parle de programmation
mixte (PM) où certaines variables seulement doivent être entières. Une
des applications les plus importantes de la PNE est l'utilisation
d'énoncés de type "si ... alors" en PL. Par exemple, si on a un problème
qui dit "si x_1 > 10, alors x_2 + x_3 < 5", on peut utiliser une
nouvelle variable entière pour écrire cette implication sous forme d'une
contrainte linéaire.

La PNE peut aussi servir à résoudre des types de problèmes de transport
où on ne peut pas accepter des solutions fractionnaires. Par exemple, si
on achemine un produit en petites quantités sur une courte période de
temps.

Plus de détails à venir éventuellement !
