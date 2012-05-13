Triangulations créatives
########################
:date: 2008-09-12 16:30
:tags: maths

On peut représenter les objets tridimensionnels par des triangles collés
les uns aux autres de telle sorte qu'ils épousent les formes de l'objet.
On appelle une telle construction une triangulation. Une fois qu'on a
obtenu une triangulation, on peut la raffiner en divisant les triangles
en triangles plus petits. Cet article présentera des méthodes de
raffinement qui, lorsqu'on représente graphiquement les triangles
qu'elles produisent, génèrent des dessins dont la beauté surprend.

Raffiner une triangulation
^^^^^^^^^^^^^^^^^^^^^^^^^^

De l'animation par ordinateur au design d'aéronefs en passant par
l'imagerie médicale, les applications de l'imagerie tridimensionnelle
sont multiples. Les logiciels utilisés dans ces applications nécessitent
une représentation d'objets tridimensionnels dans un langage
compréhensible pour un ordinateur. On se heurte alors au problème de
trouver un compromis entre une représentation fidèle de l'objet initial
et une utilisation raisonnable des ressources matérielles de
l'ordinateur : processeur, mémoire vive, espace de stockage sur disque
dur, etc. Une méthode fréquemment utilisée consiste à trianguler la
surface de l'objet, c'est-à-dire à recouvrir le mieux possible la
surface de l'objet par des triangles, puis à raffiner cette
triangulation initiale pour obtenir une meilleure représentation
|image0|
des courbes de cette surface. On arrête de raffiner lorsque
les calculs impliqués deviennent trop exigeant pour l'ordinateur.
L'image ci-contre montre un exemple d'un objet tridimensionnel, une
tête, et de trois triangulations de celle-ci. Les deux triangulations de
droite sont des raffinements de celle de gauche. Les raffinements
comptent beaucoup plus de triangles et semblent épouser les contours du
visage beaucoup mieux.

Raffinement par division de triangles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image1| Une idée qu'on peut exploiter pour raffiner une
triangulation consiste à diviser chacun des triangles existants en
plusieurs triangles. En choisissant un point à l'intérieur d'un triangle
et en faisant passer des droites par ce point et par chacun des sommets,
le triangle initial est divisé en six triangles plus petits. En
appliquant cet algorithme simple, qui est illustré ci-dessous, à une
triangu lation, on obtient un raffinement. Chaque fois qu'on répète
cette division, le nombre de triangle est multiplié par six. Donc après
*k* itérations (i.e. : répétitions), le nombre de triangles initial est
multiplié par 6\ :sup:`k`.

Il existe une infinité de choix pour le point à l'intérieur du triangle.
Chacun de ces choix engendrera des triangles différents. En général, les
triangles longs et étroits sont moins utiles pour représenter des
courbes. On leur préfère des triangles plus semblables à un triangle
équilatéral. Il faut donc à trouver un point spécifique à l'intérieur du
triangle qui servira à le diviser et qui engendrera le plus possible des
triangles "presque" équilatéraux.

Une représentation abstraite de tous les triangles par un triangle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Un résultat élémentaire de géométrie euclidienne dit que tous les
triangles qui ont les mêmes angles sont semblables ; c'est-à-dire que si
deux triangles ont les mêmes trois angles, un de ces triangles est un
agrandissement de l'autre. On appelle une homothétie l'agrandissement ou
le rapetissement qui permet de passer d'un triangle à l'autre. Puisque
l'objectif de nos raffinement est de trouver des triangles qui sont
proches d'un triangle équilatéral, on n'a pas à se soucier de la taille
de ces triangles, tout ce qui compte, ce sont les trois angles.
En somme, à une homothétie près, tous les triangles sont spécifiés
uniquement par leurs trois angles. La somme des angles d'un triangle est
180° et chaque angle est compris entre 0° et 180° exclusivement. Si on
nomme les angles *x*, *y* et *z*, on aura donc :
|image2|

-  0 < *x* < 180
-  0 < *y* < 180
-  0 < *z* < 180
-  *x* + *y* + *z* = 180

On peut interpréter les angles comme trois coordonnées dans l'espace
cartésien en trois dimensions. Les points de l'espace cartésien qui
correspondent aux quatre contraintes ci-haut forment une section de plan
de forme triangulaire que nous appellerons *T* (voir figure ci-contre).
Ce sous ensemble de l'espace cartésien est donc une représentation
abstraite de tous les triangles imaginables. Le point central de *T* est
le triangle équilatéral. Les points proches des côtés de *T* sont des
triangles dont au moins un angle est très petit et qui sont donc très
allongés.

Histogrammes de raffinement
^^^^^^^^^^^^^^^^^^^^^^^^^^^

On peut choisir un triangle et un point donné à l'intérieur des
triangles pour faire un raffinement. On raffine notre triangle initial
un grand nombre de fois pour obtenir plusieurs petits triangles. Chacun
de ces petits triangles peut être représenté par un point noir dans *T*.
Selon le nombre de triangles présents dans chaque région de *T*, il y
aura plus ou moins de points noirs et on obtiendra une région plus ou
moins sombre. L'image qu'on obtient est un histogramme de densité de
points.

Ci-dessous se trouvent des histogrammes obtenus à partir de différents
points à l'intérieur des triangles. On retrouve, dans l'ordre, la
méthode de la bissectrice, la méthode du point de Gergonne et la méthode
du point de Lemoine. (Ces images ont été obtenue grâce à la courtoisie
de Steve Butler.)
|image3|
|image4|
|image5|
En plus d'avoir une certaine qualité esthétique, ces images donnent de
l'information sur l'utilité des points intérieurs utilisés. On constate
que pour la méthode de la bissectrice, le centre de *T* est assez sombre
donc beaucoup de triangles presque équilatéraux sont produits ce qui est
excellent.

Le point de Gergonne donne un histogramme qui ressemble à un neurone.
Les points sont concentrés dans une toute petite région ce qui signifie
que les triangles obtenus ont tous une forme bien particulière.
Même si le point de Lemoine est le moins utile pour faire des
raffinements en raison du grand nombre de triangles étroits qu'il
produit (en effet, on constate que les côtés de *T* sont sombres), c'est
celui qui génère, à mon avis, le plus bel histogramme.

La transformation de *T*
^^^^^^^^^^^^^^^^^^^^^^^^

À la section précédente on s'est intéressé à l'effet d'un choix de point
intérieur sur un triangle donné après un grand nombre d'itération. On
peut aussi examiner l'effet de ce choix sur l'ensemble de *T* après une
itération. L'algorithme prend des triangles de *T* et les envoie vers
d'autres triangles de *T* : il modifie donc complètement l'ensemble des
triangles.
On peut visualiser ce qui se passe en divisant *T* en plusieurs régions
(qu'on prend triangulaire parce qu'il est plus facile de diviser un
triangle en triangles plutôt qu'en dodécagones) qu'on colore en noir et
blanc. Puis, on applique l'algorithme à tous les triangles et on observe
où les triangles fils obtenus se retrouvent dans *T*. En gardant les
mêmes divisions et les mêmes colorations, on obtient une carte de la
disposition des triangles fils.
Ci-dessous, dans l'ordre, T divisé en régions, la méthode du point de
Gergonne, la méthode du point de Lemoine et la méthode de la médiane.
(Images courtoisie de Steve Butler.)
|image6|
|image7|
|image8|
|image9|

Conclusion
^^^^^^^^^^

Les histogrammes obtenus par le raffinement de triangulations
ressemblent à des dessins au fusain. On y retrouve une symétrie
évidente, des dégradés surprenant et des formes étrangement organiques.
Les diagrammes des transformations de *T* font penser à certaines
gravures d'Escher.

L'étude des raffinements avait pour but de faciliter la modélisation
tridimensionnelle, et, comme sous-produit de cette étude, des images
très belles sont apparues. Place à la créativité triangulaire !
*Remerciements* : je tiens à remercier Steve Butler pour m'avoir fourni
ses images et m'avoir permis de les utiliser sur ce site. Je remercie
également `Ron Graham`_ et `Steve Butler`_ pour m'avoir initié aux
raffinements de triangulations lors de CCCG 2008.

.. figure:: https://blogger.googleusercontent.com/tracker/697344570467959391-5005068235951720029?l=mathfou.blogspot.com
   :align: center
   :alt: 

.. _|image10|: http://gts.sourceforge.net/gallery/heads.png
.. _|image11|: http://1.bp.blogspot.com/_HyYHulp_e30/SMqSR_7xQxI/AAAAAAAABes/C4nix5PDPes/s1600-h/divisetriangle.png
.. _|image12|: http://2.bp.blogspot.com/_HyYHulp_e30/SMqTX2kOHAI/AAAAAAAABe0/HxV1VTHq9J4/s1600-h/plantriangle.jpg
.. _|image13|: http://2.bp.blogspot.com/_HyYHulp_e30/SMqUjftUt_I/AAAAAAAABe8/nP0mYxG1li8/s1600-h/Bisector_Histogram.jpg
.. _|image14|: http://4.bp.blogspot.com/_HyYHulp_e30/SMqUjmEtpoI/AAAAAAAABfE/IUiNwlbNr3M/s1600-h/Gergonne_Histogram.jpg
.. _|image15|: http://3.bp.blogspot.com/_HyYHulp_e30/SMqUjgnQodI/AAAAAAAABfM/dQhH3Lb6le8/s1600-h/Lemoine_Histogram.jpg
.. _|image16|: http://3.bp.blogspot.com/_HyYHulp_e30/SMqVYhFMJhI/AAAAAAAABfU/17EEA3nKt2w/s1600-h/unmapped.jpg
.. _|image17|: http://3.bp.blogspot.com/_HyYHulp_e30/SMqVYy73NMI/AAAAAAAABfc/CX8YHsSOxt4/s1600-h/Gergonne_map.jpg
.. _|image18|: http://1.bp.blogspot.com/_HyYHulp_e30/SMqVY5sxIjI/AAAAAAAABfk/d-bXSuNzzNc/s1600-h/Lemoine_map.jpg
.. _|image19|: http://4.bp.blogspot.com/_HyYHulp_e30/SMqVZN8LmVI/AAAAAAAABfs/TxG37nzgN7o/s1600-h/median_map.jpg
.. _Ron Graham: http://www.math.ucsd.edu/%7Efan/ron/
.. _Steve Butler: http://www.math.ucsd.edu/%7Esbutler/

.. |image0| image:: http://gts.sourceforge.net/gallery/heads.png
.. |image1| image:: http://1.bp.blogspot.com/_HyYHulp_e30/SMqSR_7xQxI/AAAAAAAABes/C4nix5PDPes/s320/divisetriangle.png
.. |image2| image:: http://2.bp.blogspot.com/_HyYHulp_e30/SMqTX2kOHAI/AAAAAAAABe0/HxV1VTHq9J4/s320/plantriangle.jpg
.. |image3| image:: http://2.bp.blogspot.com/_HyYHulp_e30/SMqUjftUt_I/AAAAAAAABe8/nP0mYxG1li8/s400/Bisector_Histogram.jpg
.. |image4| image:: http://4.bp.blogspot.com/_HyYHulp_e30/SMqUjmEtpoI/AAAAAAAABfE/IUiNwlbNr3M/s400/Gergonne_Histogram.jpg
.. |image5| image:: http://3.bp.blogspot.com/_HyYHulp_e30/SMqUjgnQodI/AAAAAAAABfM/dQhH3Lb6le8/s400/Lemoine_Histogram.jpg
.. |image6| image:: http://3.bp.blogspot.com/_HyYHulp_e30/SMqVYhFMJhI/AAAAAAAABfU/17EEA3nKt2w/s400/unmapped.jpg
.. |image7| image:: http://3.bp.blogspot.com/_HyYHulp_e30/SMqVYy73NMI/AAAAAAAABfc/CX8YHsSOxt4/s400/Gergonne_map.jpg
.. |image8| image:: http://1.bp.blogspot.com/_HyYHulp_e30/SMqVY5sxIjI/AAAAAAAABfk/d-bXSuNzzNc/s400/Lemoine_map.jpg
.. |image9| image:: http://4.bp.blogspot.com/_HyYHulp_e30/SMqVZN8LmVI/AAAAAAAABfs/TxG37nzgN7o/s400/median_map.jpg
.. |image10| image:: http://gts.sourceforge.net/gallery/heads.png
.. |image11| image:: http://1.bp.blogspot.com/_HyYHulp_e30/SMqSR_7xQxI/AAAAAAAABes/C4nix5PDPes/s320/divisetriangle.png
.. |image12| image:: http://2.bp.blogspot.com/_HyYHulp_e30/SMqTX2kOHAI/AAAAAAAABe0/HxV1VTHq9J4/s320/plantriangle.jpg
.. |image13| image:: http://2.bp.blogspot.com/_HyYHulp_e30/SMqUjftUt_I/AAAAAAAABe8/nP0mYxG1li8/s400/Bisector_Histogram.jpg
.. |image14| image:: http://4.bp.blogspot.com/_HyYHulp_e30/SMqUjmEtpoI/AAAAAAAABfE/IUiNwlbNr3M/s400/Gergonne_Histogram.jpg
.. |image15| image:: http://3.bp.blogspot.com/_HyYHulp_e30/SMqUjgnQodI/AAAAAAAABfM/dQhH3Lb6le8/s400/Lemoine_Histogram.jpg
.. |image16| image:: http://3.bp.blogspot.com/_HyYHulp_e30/SMqVYhFMJhI/AAAAAAAABfU/17EEA3nKt2w/s400/unmapped.jpg
.. |image17| image:: http://3.bp.blogspot.com/_HyYHulp_e30/SMqVYy73NMI/AAAAAAAABfc/CX8YHsSOxt4/s400/Gergonne_map.jpg
.. |image18| image:: http://1.bp.blogspot.com/_HyYHulp_e30/SMqVY5sxIjI/AAAAAAAABfk/d-bXSuNzzNc/s400/Lemoine_map.jpg
.. |image19| image:: http://4.bp.blogspot.com/_HyYHulp_e30/SMqVZN8LmVI/AAAAAAAABfs/TxG37nzgN7o/s400/median_map.jpg
