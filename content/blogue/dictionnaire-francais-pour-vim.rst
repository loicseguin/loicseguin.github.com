Dictionnaire français pour Vim
##############################
:date: 2011-12-22 23:45
:tags: informatique

Vim possède un correcteur d'orthographe. On peut l'activer avec

.. code-block:: vim

    :set spell

puis on passe à l'erreur suivante avec ``]s``.

Par défaut, seuls des dictionnaires anglais sont fournis avec MacVim.
Installer un dictionnaire français se fait automatiquement si on définit
la variable spelllang pour le français :

.. code-block:: vim

    :set spelllang=fr

Ensuite, il ne reste plus qu'à activer la correction automatique et à
regarder MacVim se connecter à un serveur ftp pour y télécharger les
fichiers nécessaires.
Information trouvée dans les archives de comp.editors sur usenet
(`http://newsgroups.derkeiler.com/Archive/Comp/comp.editors/2006-04/msg00241.html`_).

.. _`http://newsgroups.derkeiler.com/Archive/Comp/comp.editors/2006-04/msg00241.html`: http://newsgroups.derkeiler.com/Archive/Comp/comp.editors/2006-04/msg00241.html
