Polices de caractères personnalisées dans matplotlib
====================================================

:date: 2012/12/24
:author: Loïc Séguin-Charbonneau
:tags: programmation
:status: draft


.. code:: python

    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm

    font = fm.FontProperties(
            family = 'Complex', fname = '/Users/loic/Library/Fonts/complex.ttf')

    plt.plot(range(10))
    ax = plt.gca()
    ax.set_yticklabels(ax.get_yticks(), fontproperties=font)
    ax.set_xticklabels(ax.get_xticks(), fontproperties=font)
    plt.title('Everything is crazy!!!', size=32, fontproperties=font)
    plt.savefig('stuff.pdf')
    plt.show()
