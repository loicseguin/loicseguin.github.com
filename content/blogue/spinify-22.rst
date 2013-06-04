Spinify 2.2
###########
:date: 2010-03-02 03:30
:tags: informatique, maths, physique

Je viens tout juste de lancer la nouvelle version du logiciel de
simulation numérique du modèle d'Ising Spinify. La version 2.2 comporte
plusieurs corrections de bogues de même qu'une réécriture complète de
l'interface en ligne de commande (CLI). Vous pouvez télécharger le
programme sur bitbucket: `spinify-2.2.tar.gz`_.
L'usager peut maintenant configurer tous les paramètres utilisés dans la
simulation de même que dans la génération des graphes. Ces paramètres
peuvent être spécifiés à la ligne de commande ou dans un fichier de
configuration qui sera lu par le programme. Tous les détails sont
disponibles dans la page de manuel de spinify(1).
De plus, cette version introduit de nouvelles quantités mesurables lors
de la simulation. L'usager peut maintenant choisir parmi l'énergie
interne par site, la magnétisation et la susceptibilité magnétique.
Autant d'outils pour analyser le comportement du modèle aux abords de la
température critique (de même que pour trouver cette température
critique).
Enfin, j'utilise maintenant GNU Autotools pour compiler le logiciel. En
théorie, Spinify devrait compiler sans problème sur n'importe quel
système Unix ou Linux.
Si vous utilisez ce logiciel et que vous avez des commentaires ou que
vous avez des questions à son propos, n'hésitez pas à me contacter par
l'entremise de la liste d'envoi `spinify-discuss@googlegroups.com`_.

.. _spinify-2.2.tar.gz: http://bitbucket.org/loicseguin/spinify/downloads/spinify-2.2.tar.gz
.. _spinify-discuss@googlegroups.com: mailto:spinify-discuss@googlegroups.com

