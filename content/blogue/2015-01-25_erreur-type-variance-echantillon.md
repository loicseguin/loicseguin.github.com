title: Erreur-type et variance d'un échantillon
author: Loïc Séguin-C.
date: 2015-01-25
tags: statistique
summary: L'objectif de ce billet est de comprendre la forme de deux quantités
    utilisées très fréquemment en statistique : l'erreur-type de la
    moyenne d'un échantillon
    \\[ S_m = \frac{S}{\sqrt{n}} \\]
    et la variance d'un échantillon
    \\[ S^2 = \frac{1}{n - 1} \sum_{i = 1}^n (X_i - \bar{X})^2. \\]
    Pourquoi y a-t-il un \\(n - 1\\) dans la variance? Pourquoi y a-t-il une
    racine carrée de la taille de l'échantillon dans l'erreur-type? Et que veut
    dire *erreur-type*?

[TOC]

## Introduction

L'objectif de ce billet est de comprendre la forme de deux quantités utilisées
très fréquemment en statistique : l'erreur-type de la moyenne d'un
échantillon
\\[
  S_m = \frac{S}{\sqrt{n}}
\\]
et la variance d'un échantillon
\\[
  S^2 = \frac{1}{n - 1} \sum_{i = 1}^n (X_i - \bar{X})^2.
\\]
Pourquoi y a-t-il un \\(n - 1\\) dans la variance? Pourquoi y a-t-il une racine
carrée de la taille de l'échantillon dans l'erreur-type? Et que veut
dire *erreur-type*?

## Échantillonnage

La variance d'un échantillon et l'erreur-type de la moyenne d'un échantillon
font toutes deux référence à un **échantillon**. Qu'est-ce qu'un échantillon?

Commençons par définir une **population**. Une population est l'ensemble de
tous les individus à propos desquels nous cherchons à obtenir de l'information.
Nous utiliserons \\(N\\) pour désigner le nombre d'individus dans la population.
Ici, individus est employé dans un sens large : il peut s'agir de personnes,
comme lorsqu'on parle de la population d'un pays, mais il peut aussi s'agir de
capitaux si on s'intéresse au cours de la bourse, de durées d'appels
téléphoniques, de mesures expérimentales de résistance électrique, etc. En
général, il est difficile d'obtenir des données sur *tous* les individus d'une
population et nous devons nous contenter d'étudier un sous-ensemble de la
population.

Un **échantillon** est un sous-ensemble d'une population sélectionné au hasard.
Nous utiliserons \\(n\\) pour désigner le nombre d'individus dans un
échantillon. Puisque l'échantillon est plus petit que la population, il est
plus facile d'obtenir des données sur tous les membres de l'échantillon. À
partir de ces données, nous pouvons essayer de déduire de l'information sur la
population; c'est ce qu'on appelle une **inférence statistique**.

Un exemple concret peut aider à fixer les idées. Supposons qu'on cherche à
connaître la taille moyenne des Canadiens. La population est l'ensemble de tous
les habitants du Canada et la variable d'intérêt est la taille. Évidemment, il
est impossible de parcourir le Canada en entier et de mesurer la taille de tous
ses habitants. Par conséquent, nous devons construire un échantillon en
choisissant au hasard quelques Canadiens.

La taille d'un individu \\(i\\) choisi au hasard dans la population est une
variable aléatoire \\(X_i\\)[^varalea].  L'espérance de la taille de cet
individu est la **moyenne de la population** que nous notons par \\(\mu\\).
En supposant que chaque Canadien a autant de chance d'être choisi, la
probabilité de choisir un individu en particulier parmi les \\(N\\) habitants
du Canada est de \\(1/N\\) ce qui signifie que la fonction de masse pour la
taille d'un Canadien est \\(f(x) = P(X_i = x) = 1/N\\). Par conséquent,
l'espérance de \\(X_i\\) est

\\[
\mu = \mathrm{E}[X_i] = \sum_{j = 1}^N f(x_j) x_j = \frac{1}{N} \sum_{j = 1}^N x_j
\\]

Pour un échantillon particulier, nous pouvons aussi calculer une valeur
moyenne. Cette valeur est la **moyenne de l'échantillon** :

\\[
\bar{X} = \frac{1}{n} \sum_{i = 1}^n X_i
\\]

Puisque les \\(X_i\\) sont aléatoires, la moyenne de l'échantillon est aussi
une variable aléatoire. La moyenne de l'échantillon sera probablement
différente de la moyenne de la population et un échantillon différent aura
probablement une moyenne différente. La moyenne d'un échantillon est donc un
**estimateur** de la moyenne de la population.

Cet estimateur est **non biaisé** parce que si nous calculons son espérance,
nous obtenons la moyenne de la population. Autrement dit, si nous construisons
plusieurs échantillons, que nous calculons la moyenne de chacun d'entre eux et
que nous calculons la moyenne de ces moyennes, le résultat sera très
probablement la moyenne de la population. L'écart-type des moyennes des
échantillons est ce qu'on appelle l'**erreur-type de la moyenne**[^erreurtype].
Nous calculerons l'erreur-type de la moyenne à la [section
suivante](#erreur-type-de-la-moyenne).

La variance des \\(X_i\\) est la **variance de la population**

\\[
\begin{align} \sigma^2 &= \mathrm{E}\left[ (X_i - \mu)^2 \right] \\\\
                       &= \frac{1}{N} \sum_{j = 1}^N (x_j - \mu)^2
\end{align}
\\]

Encore une fois, nous voulons utiliser l'information sur l'échantillon pour
estimer la variance de la population. La variance de l'échantillon est une
variable aléatoire qui sert d'estimateur pour la variance de la population. Le
premier réflexe est de tenter de définir la variance de l'échantillon par

\\[
S^2 = \frac{1}{n} \sum_{i = 1}^n \left(X_i - \bar{X} \right)^2
\\]

Cette formule est utilisée par certains (entre autre parce qu'elle maximise la
vraisemblance), mais elle a le désavantage d'être biaisée. Si nous calculons la
variance de plusieurs échantillons en utilisant cette formule et que nous
calculons ensuite la moyenne de ces variances, nous n'obtiendrons pas la
variance de la population. Un estimateur de la variance non biaisé est donné à
la section [Variance](#variance).

[^varalea]: La taille d'une personne n'est pas aléatoire : je mesure 178 cm et
  Camille mesure 165 cm. Par contre, si nous choisissons une personne au
  hasard, la taille que nous obtiendrons est aléatoire. Si la population ne
  consiste que de Camille et moi, la probabilité que la taille d'une personne
  choisie au hasard dans cette population soit 178 cm est de 50% et la
  probabilité qu'elle soit de 165 cm est aussi de 50%.

[^erreurtype]: En général, l'erreur-type d'une statistique est l'écart-type de
  cette statistique.

## Erreur-type de la moyenne

L'erreur-type de la moyenne, \\(S_m\\) est l'écart-type de la moyenne d'un
échantillon.  Commençons par calculer la variance de la moyenne d'un
échantillon :
\\[
\begin{align}
S_m^2 &= \mathrm{Var} \left[ \bar{X} \right] \\\\
    &= \mathrm{E} \left[ \left(\bar{X} - \mathrm{E} [\bar{X}]\right)^2 \right]
\end{align}
\\]
L'espérance de \\(\bar{X}\\) se calcule directement en utilisant la linéarité
de l'espérance et la définition de la moyenne de la population :
\\[
\begin{align}
\mathrm{E}[\bar{X}] &= \mathrm{E} \left[ \frac{1}{n} \sum_{i=1}^n X_i \right] \\\\
    &= \frac{1}{n} \sum_{i=1}^n \mathrm{E} [X_i] \\\\
    &= \frac{1}{n} \sum_{i=1}^n \mu \\\\
    &= \mu 
\end{align}
\\]
Ceci démontre que la moyenne d'un échantillon est un estimateur non biaisé de
la moyenne de la population.

En substituant ce résultat dans l'expression pour le carré de l'erreur-type
nous obtenons
\\[
\begin{align}
S_m^2 &= \mathrm{E} \left[ \left( \bar{X} - \mu \right)^2 \right] \\\\
      &= \mathrm{E} \left[ \bar{X}^2 - 2 \mu \bar{X} + \mu^2 \right] \\\\
      &= \mathrm{E} \left[ \bar{X}^2 \right]
         - 2\mu \mathrm{E} \left[ \bar{X} \right] + \mu^2 \\\\
      &= \mathrm{E} \left[ \bar{X}^2 \right] - \mu^2
\end{align}
\\]
Il ne reste qu'à déterminer la valeur du premier terme à droite de l'égalité.
Les premières étapes ne sont qu'un peu d'algèbre et l'utilisation de la
linéarité de l'espérance.
\\[
\begin{align}
\mathrm{E}\left[ \bar{X}^2 \right] &= \mathrm{E}\left[ \left(\frac{1}{n} \sum_{j=1}^n X_j \right)^2 \right] \\\\
    &= \frac{1}{n^2} \mathrm{E}\left[ \sum_{i=1}^n\sum_{j=1}^n X_iX_j \right] \\\\
    &= \frac{1}{n^2} \mathrm{E}\left[ \sum_{i=1}^n\sum_{\substack{j=1 \\ j \ne i}}^n X_iX_j + \sum_{i=1}^n X_i^2 \right] \\\\
    &= \frac{1}{n^2} \left( \sum_{i=1}^n\sum_{\substack{j=1 \\ j \ne i}}^n \mathrm{E}\left[ X_iX_j \right] + \sum_{i=1}^n \mathrm{E}\left[ X_i^2 \right] \right) \\\\
\end{align}
\\]
Si nous supposons que les variables \\(X_i\\) et \\(X_j\\) sont indépendantes,
l'espérance du produit \\(X_iX_j\\) avec \\(i\ne j\\) est le produit des
espérances[^indep],
\\[\mathrm{E}[X_iX_j] = \mathrm{E} [X_i] \mathrm{E}[X_j] = \mu^2.\\]
L'espérance de \\(X_i^2\\) est liée à la définition de la
variance de la population. En effet,
\\[
\begin{align}
\sigma^2 &= \mathrm{E} \left[ (X_i - \mu)^2 \right] \\\\
         &= \mathrm{E} [X_i^2] - \mu^2 \\\\
\mathrm{E} [X_i^2] &= \mu^2 + \sigma^2.
\end{align}
\\]
En substituant ces deux expressions dans le calcul de l'espérance de
\\(\bar{X}^2\\), nous obtenons

\\[
\begin{align}
 \mathrm{E}\left[ \bar{X}^2 \right] 
    &= \frac{1}{n^2} \left( \sum_{i=1}^n\sum_{\substack{j=1 \\ j \ne i}}^n \mu^2
       + \sum_{i=1}^n \left(\mu^2 + \sigma^2\right) \right) \\\\
    &= \frac{1}{n^2} \left( n(n-1)\mu^2 + n\left(\mu^2 + \sigma^2\right) \right) \\\\
    &= \mu^2 + \frac{\sigma^2}{n}
\end{align}
\\]

Finalement, il ne reste qu'à substituer cette dernière expression dans
l'équation décrivant \\(S_m^2\\) :
\\[
\begin{align}
S_m^2 &= \mu^2 + \frac{\sigma^2}{n} - \mu^2\\\\
      &= \frac{\sigma^2}{n} 
\end{align}
\\]
L'erreur-type est donc
\\[
S_m = \frac{\sigma}{\sqrt{n}}.
\\]

Cette expression est très intéressante parce qu'elle nous informe sur l'impact
qu'a la taille de l'échantillon sur l'erreur que nous faisons en approximant la
moyenne de la population par la moyenne de l'échantillon. Plus l'échantillon
est grand, plus l'erreur est petite ce qui est cohérent avec le fait que
l'échantillon le plus grand possible, soit la population en entier, aura une
moyenne exactement égale à celle de la population. De plus, la relation n'est
pas proportionnelle : doubler la taille de l'échantillon ne diminue pas
l'erreur de moitié. Pour cela, il faut quadrupler la taille de l'échantillon.

En pratique, l'écart-type de la population n'est pas connu. Il est donc
impossible de déterminer la valeur exacte de l'erreur-type de la moyenne. Par
contre, nous pouvons estimer cette valeur en utilisant l'écart-type de
l'échantillon plutôt que celui de la population:
\\[
S_m = \frac{S}{\sqrt{n}}
\\]


[^indep]: Deux variables aléatoires sont indépendantes si la distribution de
  probabilité d'une des variables n'est pas affectée par la connaissance de la
  valeur de l'autre variable. Dans l'exemple de la taille des Canadiens, si les
  individus sont choisis au hasard dans toute la population, savoir qu'un des
  individus a une taille de 170 cm ne donne aucune information sur la taille
  d'un autre individu. Par contre, si on sait que l'échantillon est constitué
  exclusivement des membres du Club des Grands ou des membres du Club des
  Petits, alors savoir que la taille d'un individu est de 145 cm nous informe
  que l'échantillon est composé des membres du Club des Petits. Par conséquent,
  la taille d'un autre individu dans l'échantillon est probablement petite.
  Dans ce cas, les tailles ne sont pas indépendantes.


## Variance

Essayons maintenant de trouver un estimateur non biaisé pour la variance de la
population, c'est-à-dire qui a une espérance égale à la variance de la
population.

Supposons que l'estimateur a la même forme que le paramètre :
\\[
S^2 = \alpha \sum_{i = 1}^n \left( X_i - \bar{X} \right)^2
\\]
où \\(\alpha\\) est une constante à déterminer.
On peut récrire \\(S^2\\) différemment :
\\[
\begin{align}
S^2 &= \alpha \sum_{i = 1}^n \left( X_i^2 - 2X_i\bar{X} + \bar{X}^2 \right) \\\\
    &= \alpha \left( \sum_{i = 1}^n X_i^2 - 2 \sum_{i = 1}^n X_i\bar{X} + \sum_{i = 1}^n \bar{X}^2 \right) \\\\
    &= \alpha \left( \sum_{i = 1}^n X_i^2 - 2 \bar{X} \sum_{i = 1}^n X_i + n \bar{X}^2 \right) \\\\
    &= \alpha \left( \sum_{i = 1}^n X_i^2 - 2n \bar{X}^2 + n \bar{X}^2 \right) \\\\
    &= \alpha \left( \sum_{i = 1}^n X_i^2 - n \bar{X}^2 \right) \\\\
\end{align}
\\]
Pour passer de la troisième à la quatrième ligne, nous avons utilisé la
définition de la moyenne de l'échantillon.

L'espérance de \\(S^2\\) est
\\[
\begin{align}
\mathrm{E}\left[S^2\right] &= \mathrm{E}\left[ \alpha \left( \sum_{i = 1}^n X_i^2 - n \bar{X}^2 \right) \right] \\\\
       &= \alpha \left( \sum_{i = 1}^n \mathrm{E}\left[ X_i^2 \right] - n\mathrm{E}\left[ \bar{X}^2 \right] \right) \\\\
\end{align}
\\]

En utilisant les résultats obtenus à la section [Erreur-type de la
moyenne](#erreur-type-de-la-moyenne),
nous obtenons
\\[
\begin{align}
\mathrm{E}\left[S^2\right] &= \alpha \left( \sum_{i = 1}^n \left( \mu^2 + \sigma^2 \right) - n\left(\mu^2 + \frac{\sigma^2}{n} \right) \right) \\\\
       &= \alpha \left(n \sigma^2 + n\mu^2 - n\mu^2 - \sigma^2 \right) \\\\
       &= \alpha (n - 1) \sigma^2
\end{align}
\\]

Pour que \\(S^2\\) soit non-biaisé, il faut que \\( \mathrm{E}(S^2) = \sigma^2 \\)
et donc, \\(\alpha = \frac{1}{n - 1}\\) ce qui donne

\\[
S^2 = \frac{1}{n - 1} \sum_{i=1}^n (X_i - \bar{X})^2
\\]


## Conclusion

L'erreur-type
\\[
S_m = \frac{S}{\sqrt{n}}
\\]
mesure l'écart-type de la moyenne d'un échantillon par rapport à
la moyenne de la population. Plus l'échantillon est grand, plus l'erreur-type
est petite, et donc meilleure est l'approximation de \\(\mu\\) par
\\(\bar{X}\\).

La présence du \\(n - 1\\) au dénominateur de la variance d'un échantillon est
nécessaire si nous voulons que la variance de l'échantillon soit un estimateur
non biaisé de la variance de la population.
