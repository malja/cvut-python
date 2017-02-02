# Zadání:
#########
# Implementujte následující úlohy:
# 
# * Najděte v matici (2D poli) všechny záporné hodnoty, vraťte seznam jejich 
#   indexů.
# * Implementujte násobení dvou matic
###############################################################################

def findAllNegative( matrix ):
    """
    Najde všechny záporné hodnoty v matici a vrátí jejich indexy.

    Parametry:
    ----------
        matrix: list
            2D pole reprezentující matici

    Vrací:
        list
            2D pole s indexy záporných hodnot z matice.
    """
    indexes = []

    for x in matrix:
        for y in matrix[x]:

            if matrix[x][y] < 0:
                indexes.append( [x,y] )

    return indexes