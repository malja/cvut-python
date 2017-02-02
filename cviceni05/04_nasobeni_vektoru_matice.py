# Zadání:
#########
#
# Napište funkci multiVecMat(v,m), která vypočte součin vektoru v a matice m.
#
# Pokud nesouhlasí rozměry matice a vektoru, pak funkce vrací None.
#
# Otestujte Váš program na těchto datech:
#
#    m=[[0,0,1],[0,1,0],[1,0,0]]
#    v=[2, 4, 6]
#
###############################################################################

def multiVecMat( vector, matrix ):
    """
    Pronásobí matici vektorem zprava.

    Parametry:
    ----------
        vector: list
            Vektor
        matrix: list
            Pronásobená matice. Její dimenze se musí shodovat s dimenzí
            vektoru.

    Vrací:
        list
            Pole velikosti vektoru.
    """

    # Vytvoří pole o velikosti vektoru
    result = [0] * len( matrix[0] )

    # Projde matici po řádcích
    for r, row in enumerate( matrix ):

        # Pokud nesedí rozměry, končíme
        if len(row) != len(vector):
            return None

        # Projde každý prvek v řádku
        for i, elem in enumerate( row ):

            # K poli s výsledkem přičte na index aktuálního řádku výsledek
            # násobení aktuálního prvku v řádku a jemu odpovídajícího 
            # prvku z vektoru.
            result[r] += elem * vector[i]

    return result

print( multiVecMat( [2, 4, 6], [[0,0,1],[0,1,0],[1,0,0]] ) )
