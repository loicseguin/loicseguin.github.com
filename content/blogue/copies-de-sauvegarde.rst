Copies de sauvegarde
####################
:date: 2009-03-11 03:06
:tags: informatique
:summary: Script utilisant ``rsync``.

J'ai finalement trouvé une solution convenable pour faire des copies de
sauvegarde de mes documents importants : un shell script maison assez
simple qui utilise le logiciel rsync (`informations sur ce site`_).
rsync est un logiciel libre distribué sous licence GPL et disponible sur
la plupart des plateformes Unix de même que sur MS Windows.
Si vous utilisez Mac OS X, rsync fait déjà partie de l'installation par
défaut. Il en est probablement de même pour les distributions de Linux
les plus populaires. Sur OpenBSD, vous pouvez l'installer avec la
commande :

::

    sudo pkg\_add rsync

en supposant que vous avez déjà configuré sudo et que la variable
d'environnement PKG\_PATH est définie.
Alors voici, j'ai un Macbook qui fonctionnne sous Mac OS X et il est
relié à deux disques durs externes : Hercule et Astro. Il y a plusieurs
dossiers et quelques fichiers de configuration (les dotfiles) que je
veux copier. Le script ressemble à ceci.
Mis à jour le 12 mars 2009:

.. code:: bash

    #!/bin/sh
    # This script makes a backup of important files in
    # my home directory to two external hard drives,
    # Hercule and Astro, using rsync.
    OPTS="-avuzC --delete --exclude-from=$HOME/.rsync/excludes"
    FOLDERS="Desktop Documents Music Movies Programmes Sites \
             Applescripts Pictures Jeux Library/Colorsync \
             Library/Thunderbird .rsync"
    FOLDER1="Library/Application Support"
    BACKUPDIR="Macbook backup"
    DOTFILES="$BACKUPDIR/dotfiles"
    FILES=".emacs .vimrc .profile"
    VOLUMES="/Volumes/Astro /Volumes/Hercule"
    
    for v in $VOLUMES; do
      if [ -d "$v" ]; then
        if [ ! -d "$v/$BACKUPDIR/Library" ]; then
          mkdir -p "$v/$BACKUPDIR/Library"
          echo "created directory" "$v/$BACKUPDIR/Library"
        fi
        
        for d in $FOLDERS "$FOLDER1"; do
          rsync $OPTS "$HOME/$d/" "$v/$BACKUPDIR/$d/"
        done
    
        if [ ! -d "$v/$DOTFILES" ]; then
          mkdir "$v/$DOTFILES"
          echo "created directory" "$v/$DOTFILES"
        fi
    
        for f in $FILES; do
          rsync $OPTS "$HOME/$f" "$v/$DOTFILES/$f"
        done
      
      else
         echo "ERROR:" "$v" "not mounted"
      fi
    done

Et le fichier .rsync/excludes contient

::

    .DS\_Store
    .depend
    \*.aplibrary
    .localized

Tout d'abord, on définit les options pour rsync :

-  a : le mode archivage (c'est ce qui convient le mieux pour les copies
   de sauvegarde)
-  v : afficher les opérations effectuées à l'écran
-  u : update, i.e. : si un fichier sur dans la copie de sauvegarde est
   plus récent que celui sur le Macbook, on ne le recopie pas
-  z : compresser les données
-  C : exclure tous les fichiers normalement exclus par CVS (e.g. :
   \*.o, \*~, \*.a)
-  --delete : si un fichier a été effacé du Macbook, l'effacer du
   dossier de sauvegarde
-  --exclude-from : précise le nom du fichier contenant la liste des
   exclusions

Ensuite on définit les variables qui précise les fichiers et dossiers à
copier. On a une boucle pour effectuer les opérations sur les deux
disques durs externes puis une autre pour effectuer les copies de tous
les dossiers voulus.
Le dossier Library/Application Support a sa propre variable car
j'obtiens des erreurs si je l'inclus dans la liste FOLDERS. J'ai essayé
de l'inclure avec des guillemets, en échappant l'espace
(Library/Application\\ Support) mais rien ne fonctionnait. Si quelqu'un
sait comment faire en sorte que je puisse include ce dossier dans la
liste avec les autres, faites-moi le savoir.
Je mets les fichiers de configuration dans un dossier nommé dotfiles que
je crée s'il n'existe pas déjà.
J'ai copié le script dans un dossier qui fait partie de mon $PATH. Voilà
! C'est fait ! Des copies de sauvegarde facile en tapant backup dans un
terminal. La magie de rsync, c'est que le logiciel ne recopie que les
fragments de fichiers qui ont été modifiés depuis la dernière
sauvegarde. Donc le processus est très rapide en général (sauf la
première fois que le script fonctionne puisqu'il doit alors copier
l'ensemble des fichiers).
Prochaine étape : synchroniser mon Macbook et mon ordinateur de bureau
roulant sous OpenBSD avec `Unison`_...

.. figure:: https://blogger.googleusercontent.com/tracker/697344570467959391-3877704818423686673?l=mathfou.blogspot.com
   :align: center
   :alt: 

.. _informations sur ce site: http://samba.anu.edu.au/rsync/
.. _Unison: http://www.cis.upenn.edu/%7Ebcpierce/unison/
