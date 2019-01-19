Extraction des données météorologiques d'Archives climatiques nationales du Canada
==================================================================================

:date: 2013-07-04
:author: Loïc Séguin-Charbonneau
:tags: programmation, données ouvertes
:summary: Il est assez facile de récupérer des données météorologiques
          historiques à partir du site web d'`Archives climatiques nationales
          du Canada`_.  Voici un petit guide pour y arriver en utilisant un
          script Python très simple.

Il est assez facile de récupérer des données météorologiques historiques à
partir du site web d'`Archives climatiques nationales du Canada`_.  Voici un
petit guide pour y arriver en utilisant un script Python très simple.

Tout d'abord, il faut identifier la station qui vous intéresse.  Vous pouvez
chercher les stations disponibles à proximité d'une ville canadienne donnée en
faisant une *Recherche spécifique* à partir de l'onglet *Données climatiques en
ligne*.  Dans mon cas, je m'intéresse aux données de la région de Montréal et
je veux des données qui remontent le plus loin possible dans le temps.  La
station la plus appropriée est donc **Montreal/Pierre Elliott Trudeau Intl A**.
En cliquant sur le bouton *Allez*, vous arriverez sur une page montrant
quelques données pour la période actuelle.  Ce qui vous intéresse, c'est la
barre d'adresse de votre navigateur.  Dans l'adresse se trouve l'identifiant de
la station ``StationID``.  Pour la station que j'ai sélectionnée, l'adresse
contient le texte suivant:

    ...&Prov=QUE&StationID=5415&hlyRange=...

Le numéro de ma station est donc 5415.  Enfin, à partir de cette page, vous
pouvez aussi déterminer la date à partir de laquelle les données sont
disponibles.  Pour Montréal, les données quotidiennes sont disponibles à partir
du premier septembre 1941.

Armé du numéro de station et de la période pour laquelle les données sont
disponibles, il ne reste qu'à les télécharger.  Je me suis créé un
répertoire pour y conserver les données.

.. code:: bash

    mkdir -p data/meteo_ca
    cd data/meteo_ca

Un fichier ``csv`` contenant toutes les données quotidiennes d'une année se trouve
à l'adresse ::

    http://climat.meteo.gc.ca/climateData/bulkdata_f.html?timeframe=2&Prov=QUE&StationID={station_id}&Month=1&Year={year}&Day=1&format=csv

Il est aussi possible de télécharger un fichier au format XML et d'obtenir des
données horaires plutôt que quotidienne.  À vous de décider ce dont vous avez
besoin.

Le script suivant récupère tous les fichiers ``csv`` et leur donne un nom
gentil.  Puisque les données pour l'année 1941 ne commencent qu'à partir du
mois de septembre, j'ai décidé d'ignorer cette année et de commencer la
collecte en 1942.

.. code:: python

    import urllib

    URL = 'http://climat.meteo.gc.ca/climateData/bulkdata_f.html?timeframe=2&Prov=QUE&StationID={station_id}&Month=1&Year={year}&Day=1&format=csv'

    for year in range(1942, 2014):
        fname, msg = urllib.urlretrieve(
                            URL.format(station_id=5415, year=year),
                            filename='meteo_{}.csv'.format(year))
        print 'Fetched', fname


Et voilà!  Évidemment, le plaisir ne fait que commencer puisqu'on peut maintenant analyser
ces données.

Pour le moment, je me contente de montrer un graphique de la température
moyenne en fonction du temps obtenu à partir du code suivant.

.. code:: python

    import pandas as pd
    import matplotlib.pyplot as plt

    frames = []
    for year in range(1942, 2014):
        frames.append(pd.read_csv('meteo_{}.csv'.format(year),
                                  skiprows=24, index_col=0, parse_dates=True,
                                  decimal=',', encoding='iso-8859-1'))

    all_years = pd.concat(frames)
    all_years.ix[:, 8].plot()
    plt.xlabel(u'Année')
    plt.ylabel(u'Température (${}^\circ$C)')
    plt.show()


.. image:: |static|/images/meteo_1942-2013.png
   :alt: Température annuelle moyenne depuis 1942




.. _`Archives climatiques nationales du Canada`: http://climat.meteo.gc.ca/Welcome_f.html
