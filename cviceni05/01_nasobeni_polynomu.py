# Zadání:
#########
# 
# Napište funkci polyMulti, která násobí dva polynomy (polynomy mohou mít různé
# stupně).
#
# Příklad volání: polyMulti( [1, 1], [-2, 1] ) vrátí [-2, -1, 1] neboť 
# (x+1)(x−2)=x^2−x−2
###############################################################################

def polyMulti( x, y ):
    """
    Provede vzájemné pronásobení dvou polynomů reprezentovaných jako pole.
    Například [1, 1] značí polynom x + 1.
    
    Parametry:
    ----------
        x: list
            První polynom
        y: list
            Druhý polynom
    
    Vrací:
    ------
        list
            Výsledek násobení polynomů x a y.
    """

    # Vytvoří pole nul o délce (x + y)-1.
    poly = [0]*(len(x)+len(y)-1)

    # Vezme po řadě všechny prvky polynomu x
    for a in range(len(x)):

        # projde všechny prvky druhého polynomu
        for b in range( len(y) ):

            # Uloží výsledek
            poly[a+b] += x[a]*y[b]

    return poly

print(polyMulti( [1, 1], [-2, 1] ))