Le problème du contrôle de groupes d'ascenseurs
###############################################
:date: 2007-10-22 17:21
:tags: recherche opérationnelle
:summary: 

Ceux qui ont déjà eu à prendre un ascenseur pour se rendre sur leur lieu
de travail quotidiennement savent à quel point il peut y avoir de
l'achalandage pour monter dans ces machines. Aux heures de pointe, il
peut y avoir des gens qui veulent monter du rez-de-chaussée à presque
tous les étages et des gens déjà à des étages supérieurs qui veulent
changer d'étage.

Lorsqu'il n'y a qu'un ascenseur, il est assez facile de gérer ses
déplacements. Une façon de faire assez répandue est de donner la
priorité au demandes faites dans la cabine (c'est-à-dire par les
personnes qui sont déjà dans l'ascenseur) et de s'arrêter aux étages où
une demande de service dans la même direction (monter ou descendre) a
été faite. Si personne n'est dans l'ascenseur, on répond en priorité à
la première demande faite.

S'il y a plusieurs ascenseurs, comme c'est le cas dans les grandes tours
à bureaux, la situation est différente. On peut gérer chaque ascenseur
indépendamment, mais cela est loin d'être optimal. Une personne qui veut
monter fera une demande de service à chaque ascenseur et monopolisera
ainsi tous les ascenseurs. Pour éviter cela, on doit contrôler le groupe
d'ascenseur comme un seul et unique système. Cependant, ce système est
très complexe et il est difficile à optimiser.

Entre autres difficultés, l'arrivée des demandes est aléatoire de même
que les destinations. Il faut minimiser le temps de transit de chaque
passager de même que le temps d'attente. On peut aussi demander à
minimiser certains paramètres reliés à l'usure ou aux coûts d'opération.
Plusieurs approches algorithmiques différentes ont été prises pour
aborder le problème. Une simple recherche sur Google donne de nombreux
liens vers des articles qui proposent des approches évolutives,
neuronales, et autres. Je vous tiendrez au courant de mes lectures...
