Résolution du problème des ponts de Königsberg
##############################################
:date: 2007-08-24 06:24
:tags: maths
:summary: 

D'abord, on doit définir ce qu'est un graphe (en fait, ce qu'on va définir ici
est appelé par certains un multigraphe). Un graphe G est simplement un ensemble
de n points qu'on appelle des sommets :math:`S = \{x_1, x_2, ..., x_n\}` reliés
par des arrêtes :math:`A = \{(x_i x_j, 1), (x_i x_j, 2), (x_k x_l, 1), ..., (x_n
x_m, 3)\}`. On remarque que chaque arrête est spécifiée par deux points (les
points qui forment les extrémités de l'arrête) et un entier qui identifie
uniquement l'arrête dans les cas où il y a plus d'une arrête entre deux même
points. En somme, pour produire un graphe, il suffit de tracer des points sur
une feuille et de les relier par autant de ligne qu'on veut.

Maintenant, on peut facilement s'imaginer que le graphe constitue un ensemble
de routes entre différents villages. Alors, on peut marcher le long de ces
routes pour aller d'un village :math:`x_1` à un village :math:`x_{11}`. On peut
spécifier le chemin qu'on a pris en donnant la liste des routes qu'on a suivit.
Par exemple on peut décrire le chemin comme étant la suite d'arrêtes
:math:`(x_1 x_4, 2), (x_4 x_8, 1), (x_8 x_5, 1), (x_5 x_11, 3)`. Si on fait un
trajet qui nous ramène au village d'où nous étions partis, on dit que ce chemin
est un tour. Un tour est eulérien (oui, vous avez deviné, en l'honneur de
Euler) s'il passe par toutes les arrêtes une et une seule fois.

Le problème des ponts de Königsberg peut donc être reformulé en terme
d'un graphe et de la possibilité de trouver un tour eulérien sur ce
graphe. Chaque lopin de terre devient un sommet de notre graphe et
chaque pont devient une arrête. Des sommets sont adjacents (i.e. : ont
un lien entre eux) si les lopins de terre sont reliés par un pont. On a
donc un graphe constitué de quatre sommets et de sept arrêtes. Alors,
est-il possible de trouver un tour eulérien sur un tel graphe ?

Le degré d'un sommet est simplement le nombre d'arrêtes qui sont
attachées à ce sommet. Si un graphe admet un tour eulérien, que peut-on
dire du degré de ses sommets ? Le tour eulérien passe par toutes les
arrêtes donc aussi par tous les sommets. Puisque chaque arrête est
utilisée une seule fois, quand le tour "arrive" à un sommet, il doit en
"repartir" par une autre arrête. Donc chaque sommet a un nombre pair
d'arrêtes (une pour l'arrivée et une pour le départ) et donc un degré
pair.

Par conséquent, si un graphe a des sommets qui n'ont pas un degré pair,
il est impossible de trouver un tour eulérien sur ce graphe. Un petit
coup d'oeil à l'image de Königsberg et on trouve tout de suite des
sommets de degré impair. Donc il est impossible de trouver un tour
eulérien et la solution au problème des ponts de Königsberg est que
c'est impossible.
