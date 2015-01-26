title: Interpolation polynômiale
author: Loïc Séguin-C.
date: 2015-02-01
status: draft

## Un coefficient de détermination égal à un est une bonne chose

Imaginez qu'on vous donne comme mission de déterminer le module de la force
exercée par la corde d'un arc sur une flèche pour différentes allonges. Vous
allez au laboratoire et, à l'aide d'un dynamomètre, vous tirez sur la corde de
l'arc pour atteindre l'allonge désirée. Vous mesurez le module de la force
indiqué sur le dynamomètre et vous répétez la procédure pour différentes
allonges. Si vous avez les ressources pour faire l'expérience, allez-y
maintenant et revenez avec vos données. Sinon, considérez les données ci-dessous
que j'ai recueillies moi-même.

| Allonge (m)  | Module de la force (N)  |
|-------------:|------------------------:|
|        0,000 |                       0 |
|        0,040 |                      19 |
|        0,080 |                      30 |
|        0,120 |                      41 |

Ces données viennent normalement avec des incertitudes expérimentales, mais,
pour les besoins de la présente discussion, elles ne sont pas nécessaires.

On peut tracer un graphique du module de la force en fonction de l'allonge qui
donne à peu près ceci.


    import numpy as np
    import matplotlib.pyplot as plt
    %matplotlib inline
    import seaborn as sns
    sns.set_style('white')


    allonge = np.array([0, 0.04, 0.08, 0.12])
    force = np.array([0, 19, 30, 41])


    fig, ax = plt.subplots(figsize=(9, 6))
    ax.scatter(allonge, force)
    ax.set_xlabel('Allonge (m)', fontsize=16)
    ax.set_ylabel('Module de la force (N)', fontsize=16)
    sns.despine()


![Module de la force exercée par un arc pour différentes allonges.](2015-01-01_interpolation-polynomiale_files/2015-01-01_interpolation-polynomiale_3_0.png)


Vous utilisez ensuite votre logiciel d'analyse de données favori pour tester
différents modèles. Par exemple, on peut essayer un modèle linéaire, quadratique
ou cubique.


    fig, ax = plt.subplots(figsize=(9, 6))
    ax.scatter(allonge, force)
    for degree in range(1, 4):
        model = np.polyfit(allonge, force, degree)
        
        yfit = np.polyval(model, allonge)
        ymean = np.mean(force)
        SS_res = np.sum((force - yfit)**2)
        SS_tot = np.sum((force - ymean)**2)
        R2 = 1 - SS_res / SS_tot
        print(R2)
        
        x = np.linspace(allonge[0] - 0.01, allonge[-1] + 0.01, 400)
        forcefit = np.polyval(model, x)
        ax.plot(x, forcefit)
    
    ax.set_xlabel('Allonge (m)', fontsize=16)
    ax.set_ylabel('Module de la force (N)', fontsize=16)
    sns.despine()

    0.979062159215
    0.996510359869
    1.0



![Trois modèles polynomiaux (degré 1 en bleu, degré 2 en vert, degré 3 en rouge).](2015-01-01_interpolation-polynomiale_files/2015-01-01_interpolation-polynomiale_5_1.png)



    model




    array([  2.08333333e+04,  -5.00000000e+03,   6.41666667e+02,
             2.13162821e-14])



## Constuire un polynôme qui passe par un ensemble de points

Si on a $N$ points $(x_i, y_i)$, il est toujours possible de trouver un polynôme
$p$ de degré au plus $N - 1$ qui passe par chacun des points. Ce polynôme est
assez simple à construire. Il doit satisfaire
$$p(x_1) = y_1 \\
p(x_2) = y_2 \\
\vdots \\
p(x_N) = y_N$$

On peut satisfaire la première égalité facilement avec $p(x) = y_1$. Évidemment,
ce polynôme ne satisfait aucune des autres égalités. Si on veut satisfaire la
deuxième égalité, on peut ajouter un terme $y_2$ et multiplier le premier terme
par $x_2 - x$ de telle sorte que lorsqu'on évalue le polynôme à $x = x_2$, le
premier terme disparaît et il ne reste que le second.

$$p(x) = y_1 (x_2 - x) + y_2$$

Malheureusement, cette version ne satisfait plus la première égalité car $p(x_1)
= y_1 (x_2 - x_1) + y_2$. On peut assez facilement rétablir la situation en
multipliant le second terme par $x_1 - x$ et en divisant le premier terme par
$x_2 - x_1$. On obtient alors le polynôme

$$p(x) = y_1 \frac{x_2 - x}{x_2 - x_1} + y_2 (x_1 - x)$$

Ce polynôme vaut $y_1$ à $x_1$ mais il vaut maintenant $y_2 (x_1 - x_2)$ à
$x_2$. Si on divise le deuxième terme par $x_1 - x_2$, on obtient un polynôme
qui satisfait les deux premières égalités.

$$p(x) = y_1 \frac{x_2 - x}{x_2 - x_1} + y_2 \frac{x_1 - x}{x_1 - x_2}$$

Ce polynôme est linéaire (degré $1$) et passe par deux points de données.

En continuant le raisonnement de la sorte, on arrive à construire le polynôme
suivant qui satisfait les $N$ égalités.

$$p(x) = \sum_{i = 1}^N y_i \frac{\Pi_{j = 1\\j \neq i}^N (x_j - x)}{\Pi_{j =
1\\j \neq i}^N (x_j - x_i)}$$

(Vérifiez que $p(x_i) = y_i$ pour $i = 1, \ldots, N$.)

Le degré de ce polynôme est déterminé par le numérateur de ses termes. Puisque
le numérateur de chaque terme contient $N - 1$ facteurs ($j$ va de $1$ jusqu'à
$N$, mais saute par-dessus la valeur $i$), le polynôme est donc de degré au plus
$N - 1$. Ce polynôme s'appelle un polynôme d'[interpolation de
Lagrange](https://fr.wikipedia.org/wiki/Interpolation_lagrangienne).

La construction du polynôme d'interpolation de Lagrange montre que pour
n'importe quel ensemble de $N$ points, il est possible de trouver un polynôme
qui passe par tous ces points et que ce polynôme a un degré au plus $N - 1$.

Calculons le polynôme d'interpolation de Lagrange pour les valeurs
expérimentales.

$$ p(x) = 20833,33 x^3 - 5000 x^2 + 641,67 x$$


    model




    array([  2.08333333e+04,  -5.00000000e+03,   6.41666667e+02,
             2.13162821e-14])



Le polynôme de degré 3 obtenu par la méthode des moindres carrés est donc
exactement le polynôme d'interpolation de Lagrange. Comme tout ensemble de
données admet un polynôme d'interpolation de Lagrange, il est certain qu'il est
possible d'obtenir un modèle avec un coefficient de détermination de 1. Cela ne
veut pas dire que le modèle est une description adéquate des données. Il faut
donc éviter de croire qu'une valeur près du coefficient de détermination près de
1 est nécessairement une indication de la qualité d'un modèle.


    
