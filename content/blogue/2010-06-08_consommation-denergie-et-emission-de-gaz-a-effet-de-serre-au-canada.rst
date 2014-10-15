Consommation d'énergie et émission de gaz à effet de serre au Canada
####################################################################
:date: 2010-06-08 03:09
:tags: environnement, python

En faisant quelques recherches sur Internet, je suis tombé sur des
données relatives à la consommation d'énergie et à l'émission de GES par
les foyers canadiens pour la période de 1990 à 2007. Ces données sont
rendues publiques par l'`Office de l'efficacité énergétique`_ de
`Ressources naturelles Canada`_. Elles proviennent principalement de
`Statistique Canada`_.

Les données sont disponible sous la forme d'un document Excel
(`res\_ca\_1\_e.xls`_). J'ai utilisé Python, Matplotlib et un module
nommé xlrd pour visualiser les données. Python et Matplotlib n'ont
probablement pas besoin de présentation. `xlrd`_ est un module qui
permet d'extraire les information d'un fichier Excel à partir de Python.
Une introduction à l'utilisation de xlrd est disponible sur
`scienceoss.com`_. Mon script Python est disponible `ici`_.

|image0|

|image1|

Je dois avouer avoir été assez surpris du faible taux d'augmentation de
la consommation d'électricité et des émissions de GES. Bien sûr, il est
navrant qu'on parle d'augmentation alors que les objectifs du protocole
de Kyoto étaient de réduire les émissions de GES par rapport à celles de
1990. Néanmoins, si l'on en croit ces données, la situation n'est pas si
terrible au Canada.


.. _Office de l'efficacité énergétique: http://oee.nrcan.gc.ca/
.. _Ressources naturelles Canada: http://www.nrcan-rncan.gc.ca/com/
.. _Statistique Canada: http://www.statcan.gc.ca/
.. _res\_ca\_1\_e.xls: http://oee.nrcan.gc.ca/corporate/statistics/neud/dpa/tablestrends2/res_ca_1_e.xls
.. _xlrd: http://www.lexicon.net/sjmachin/xlrd.htm
.. _scienceoss.com: http://scienceoss.com/read-excel-files-from-python/
.. _ici: http://devio.us/~loicseguin/econcan.py

.. |image0| image:: http://2.bp.blogspot.com/_HyYHulp_e30/TA2x4fN5FJI/AAAAAAAACAI/959Bj3crY-Y/s400/Secondary+Energy+Use+by+Energy+Source.jpg
.. |image1| image:: http://3.bp.blogspot.com/_HyYHulp_e30/TA2yKDyXtlI/AAAAAAAACAQ/DLja2Y6F03I/s400/Green+House+Gas+Emissions+by+Energy+Source.jpg
