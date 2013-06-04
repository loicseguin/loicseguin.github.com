title: Variations saisonnières des naissances au Canada
author: Loïc Séguin-C.
date: 2013-04-01
summary: Quand y a-t-il plus de naissances?

On commence par lire les données dans le fichier CSV obtenu à partir de la
[table 102-4502][table102-4502] du site de [Statistique Canada][statcan].


```r
rawdata <- read.csv("01024502-eng.csv")
```


Le fichier contient le nombre de naissances dans chaque province pour chacun
des mois de l'année, de 1991 à 2011.  Il contient également des données
combinées pour l'ensemble du Canada et pour chaque année.  Pour le moment,
seules les données pour l'ensemble du Canada sont analysées.  Dans la colonne
`GEO`, ces données contiennent la chaîne de caractère `Canada, place of
residence of mother`.  Le tableau contient également les pourcentages des
naissances pour chaque mois.  Ces pourcentages sont identifiés par la chaîne de
caractère `Percentage of live births` dans la colonne `UNIT`, alors que le
nombre de naissance est identifié par `Number of live births`.

La fonction `grepl` peut être utilisée pour éliminer toutes les lignes du
tableau de données qui ne décrivent pas l'ensemble du Canada avec des nombres
absolus pour chaque mois.  `grepl` prend une expression régulière comme premier
argument et une liste (ou un élément unique) comme second argument.  La
fonction retourne une liste de valeurs booléennes qui indique si l'expression
régulière a été trouvée à chacune des positions de la liste d'entrée.  Par
exemple,


```r
grepl("bon", c("bonjour", "allo"))
```

```
## [1]  TRUE FALSE
```


La commande suivante sélectionne toutes les lignes pour lesquelles la colonne
`GEO` commence par `Canada`, la colonne `UNIT` commence par `Number` et la
colonne `MONTHBIRTH` commence par `Month`.  De plus, seules les colonnes
d'intérêt sont retenues.  Ensuite, on renomme chaque colonne avec un nom plus
descriptif.


```r
canada.births <- rawdata[grepl("^Canada", rawdata$GEO) & grepl("^Number", rawdata$UNIT) & 
    grepl("^Month", rawdata$MONTHBIRTH), c("Ref_Date", "MONTHBIRTH", "Value")]
names(canada.births) <- c("Year", "Month", "Births")
head(canada.births)
```

```
##    Year                   Month Births
## 43 1991 Month of birth, January  32150
## 44 1992 Month of birth, January  31974
## 45 1993 Month of birth, January  30989
## 46 1994 Month of birth, January  30265
## 47 1995 Month of birth, January  29975
## 48 1996 Month of birth, January  29410
```


Le même résultat peut aussi être obtenu avec la commande `subset` :


```r
canada.births <- subset(rawdata, grepl("^Canada", GEO) & grepl("^Number", UNIT) & 
    grepl("^Month", MONTHBIRTH), select = c(Ref_Date, MONTHBIRTH, Value))
names(canada.births) <- c("Year", "Month", "Births")
head(canada.births)
```

```
##    Year                   Month Births
## 43 1991 Month of birth, January  32150
## 44 1992 Month of birth, January  31974
## 45 1993 Month of birth, January  30989
## 46 1994 Month of birth, January  30265
## 47 1995 Month of birth, January  29975
## 48 1996 Month of birth, January  29410
```


On peut simplifier le tableau en éliminant `Month of birth, ` pour n'utiliser
que le nom du mois.  Encore une fois, les expressions régulières sont parfaites
pour cette tâche.  La fonction `gsub` remplace toutes les occurences d'une
expression régulière dans une liste.  Si l'expression à trouver contient des groupes
(dénotés par des parenthèses), ces groupes peuvent être utilisés dans
l'expression de remplacement avec `\1` à `\9`.


```r
levels(canada.births$Month) <- gsub("Month of birth, ([a-zA-Z].)", "\\1", 
    levels(canada.births$Month))
head(canada.births)
```

```
##    Year   Month Births
## 43 1991 January  32150
## 44 1992 January  31974
## 45 1993 January  30989
## 46 1994 January  30265
## 47 1995 January  29975
## 48 1996 January  29410
```


Dans le tableau de données, les mois sont des niveaux, mais R ne sait pas
comment ordonner ces niveaux.  Par défaut, les niveaux décrits par des chaînes
de caractères sont ordonnés alphabétiquement.  La commande suivante place les
mois en ordre chronologique.


```r
canada.births$Month <- factor(canada.births$Month, levels = c("January", "February", 
    "March", "April", "May", "June", "July", "August", "September", "October", 
    "November", "December"))
```


Si on demande à R de tracer un graphique des naissances en fonction du mois de
l'année, il combine automatique les données de chaque année et produit les
boîtes à moustache suivantes (mieux connu en anglais sous le nom de *box
plot*).


```r
plot(canada.births$Month, canada.births$Births)
```

![plot of chunk unnamed-chunk-7](static/images/unnamed-chunk-7.png) 


Pour analyser les variations saisonnières, le nombre de naissance chaque mois
n'est pas aussi important que le pourcentage des naissances de l'année qui ont
lieu chaque mois.  Dans la figure précédente, on peut voir une certaine
variation, mais rien de très convaincant.  Le problème est qu'une grande part
des variations pour chaque mois est en fait liée à une variation annuelle du
nombre de naissances.  Il faut donc normaliser les naissances par le nombre
total de naissances dans une année (oui, cette information était déjà contenue
dans le fichier de départ, mais on peut voir comment R permet de calculer
simplement ce genre de quantité).

Le paquetage `data.table` facilite cette tâche.

```r
library(data.table)
birthstable <- data.table(canada.births)
withfrac <- birthstable[, `:=`(Birth_frac, Births/sum(Births)), by = Year]
plot(withfrac$Month, withfrac$Birth_frac)
```

![plot of chunk unnamed-chunk-8](static/images/unnamed-chunk-8.png) 


On peut aussi regarder les données pour la période de 1991 à 2011 en entier et
tenter de déterminer s'il y a bien une variation saisonnière en effectuant une
transformée de Fourier du signal.


```r
withfrac <- withfrac[with(withfrac, order(Year, Month)), ]
print(withfrac)
```

```
##      Year     Month Births Birth_frac
##   1: 1991   January  32150    0.07987
##   2: 1991  February  30259    0.07517
##   3: 1991     March  34782    0.08641
##   4: 1991     April  35314    0.08773
##   5: 1991       May  36272    0.09011
##  ---                                 
## 248: 2011    August  33564    0.08888
## 249: 2011 September  33429    0.08852
## 250: 2011   October  31884    0.08443
## 251: 2011  November  30350    0.08037
## 252: 2011  December  29497    0.07811
```

```r

ft <- fft(withfrac$Birth_frac)
nft <- length(ft)
ft <- Mod(c(ft[(nft/2 + 1):nft], ft[1:(nft/2)]))
freqs <- c(seq(-0.5, 0, length.out = (nft/2)), seq(0, 0.5, length.out = (nft/2)))
fftdata <- data.frame(freqs, ft)

plot(fftdata[130:230, ], t = "l", pch = 20, cex = 0.8, xlab = "Frequency (1/month)", 
    ylab = "Power")
freqmax <- freqs[130:230][which.max(ft[130:230])]
abline(v = freqmax, lty = 3)
text(0.1, 0.63, freqmax, adj = c(0, 0))
text(0.1, 0.6, 1/freqmax, adj = c(0, 0))
# Period axis on top
a <- axis(3, lty = 0, labels = FALSE)
axis(3, cex.axis = 0.6, labels = format(1/a, digits = 2), at = a)
```

![plot of chunk unnamed-chunk-9](static/images/unnamed-chunk-9.png) 





[table102-4502]: http://www5.statcan.gc.ca/cansim/a05?id=1024502&retrLang=eng "Table 102-4502 Live births, by month, Canada, province and territories, annual"

[statcan]: http://www.statcan.gc.ca "Statistique Canada"
