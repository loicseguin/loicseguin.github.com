Optique 101 (partie 1)
######################
:date: 2008-11-14 17:54
:tags: photographie, physique
:summary: Pour comprendre comment fonctionne la vue et comment fonctionne un
          appareil photographique, on doit d'abord connaître quelques principes
          fondamentaux d'optique géométrique. Nous verrons la propagation de la
          lumière en ligne droite, la loi de Snell-Descartes et les propriétés
          des lentilles minces.

Pour comprendre comment fonctionne la vue et comment fonctionne un
appareil photographique, on doit d'abord connaître quelques principes
fondamentaux d'optique géométrique. Nous verrons la propagation de la
lumière en ligne droite, la loi de Snell-Descartes et les propriétés des
lentilles minces.

La lumière visible est une onde électromagnétique, c'est-à-dire un champ
magnétique et un champ magnétique qui se propagent dans l'espace en
oscillant. Pour bien comprendre les phénomènes impliquant la lumière, on
doit utiliser les équations de l'électromagnétisme découvertes par James
Clerk Maxwell au XIXe siècle et la mécanique quantique du XXe siècle.
Heureusement, on peut comprendre le fonctionnement des lentilles et
miroirs en faisant plusieurs simplifications qui nous permettent
d'ignorer ces théories physiques complexes.

D'abord, on suppose que la lumière se déplace en ligne droite. Cette
ligne droite correspond à la direction de propagation du champ
électromagnétique. Pour notre analyse, il est souvent utile de
considérer des rayons de lumière. Un rayon de lumière peut, par exemple,
correspondre à la trajectoire d'un faisceau laser, ou à la lumière qui
provient du sommet de la tour Eiffel et qui parvient à votre oeil.
Deux lois fondamentales de l'optique ont d'abord été trouvées
empiriquement, puis expliquées théoriquement par les équations de
Maxwell. D'abord, la loi de la réflexion, découverte environ 1000 ans
après Jésus Christ par un arabe du nom d'Alhazen, stipule que lorsqu'un
rayon de lumière atteint une surface, l'angle d'incidence :math:`\theta_i`
et l'angle de réflexion :math:`\theta_r` (mesurés par rapport à une droite
perpendiculaire à la surface, la normale) sont égaux:
:math:`\theta_i` = :math:`\theta_r`.

|image0|

De plus, le rayon incident, le rayon réfléchi et la normale
à la surface sont dans le même plan, qu'on appelle plan d'incidence. La
lumière se comporte donc comme une boule de billard qui frappe la bande
: les angles d'incidence et de réflexion sont égaux, et la boule demeure
sur la table.

Beaucoup plus tard, en 1621, Willebrord Snell découvre la loi de la
réfraction. Cette loi, connu sous le nom de loi de Snell, a été publiée
pour la première fois dans une notation mathématique moderne par René
Descartes quelques années plus tard. Pour cette raison, on l'appelle
parfois la loi de Snell-Descartes. Lorsque la lumière passe d'un milieu
transparent à un autre (par exemple, de l'air au verre) sa vitesse
change et ce changement de vitesse, jumelé avec le principe de moindre
action (qui veut dire, grosso modo, que la lumière emprunte le chemin le
plus court possible entre deux points), entraîne un changement de
direction du rayon lumineux.

Chaque milieu transparent est caractérisé par un indice de réfraction,
noté *n*. Cet indice est le rapport entre la vitesse de la lumière dans
le vide et la vitesse de la lumière dans le milieu considéré. Par
exemple, la lumière se propage un quart de fois moins vite dans l'eau
que dans le vide ce qui donne pour l'eau :

.. math::

    n_{\mathrm{eau}} &= v_{\mathrm{vide}} / v_{\mathrm{eau}} \\
    n_{\mathrm{eau}} &= v_{\mathrm{vide}} / ((1 - 1/4)v_{\mathrm{vide}}) \\
    n_{\mathrm{eau}} &= 1,33

La loi de Snell-Descartes fait le lien entre les indices de réfraction
et les angles d'incidence et de réfraction. Si un rayon de lumière passe
du milieu 1 au milieu 2, d'indices de réfraction :math:`n_1` et
:math:`n_2` respectivement, a un angle d'incidence :math:`\theta_i`,
alors l'angle du rayon transmis :math:`\theta_t` respectera la relation :

.. math::

    n_1 \sin \theta_i = n_2 \sin \theta_t

|image1|

De plus, le rayon incident, le rayon transmis et la normale sont dans le
même plan, comme pour la réflection.
Le milieu le plus réfringent est celui avec l'indice de réfraction le
plus élevé. Si le rayon lumineux passe du milieu le moins réfringent au
milieu le plus réfringent, il se
rapprochera de la normale. S'il passe du milieu le plus réfringent au
milieu le moins réfringent, il s'éloignera de la normale.
La loi de Snell-Descartes est fondamentale pour comprendre le
fonctionnement d'une partie cruciale d'un appareil photo : la lentille.
Nous verrons dans le prochain article comment fonctionne une lentille.


.. |image0| image:: http://4.bp.blogspot.com/_HyYHulp_e30/SR4adIhjfXI/AAAAAAAABmw/_CTRYJxATfQ/s400/reflexion.png
.. |image1| image:: http://4.bp.blogspot.com/_HyYHulp_e30/SR4adZz-6II/AAAAAAAABm4/dQsj1m_xJcM/s400/refraction.png
