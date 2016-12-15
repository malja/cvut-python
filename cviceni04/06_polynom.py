# Zadání:
#########
# 
# Napište funkci printPoly,která vypíše polynom, přičemž mocniny bude tisknout
# znakem '^'.
#
# Pokud je nějaký koeficient nulový, příslušný člen se nevypíše
# 
# Příklad: printPoly( [ 1, 1, 0, -2] ) vytiskne 1 + x - 2 x^3
###############################################################################

def sign( number ):
    """
    Vrátí znaménko čísla jako řetězec
    Parametry:
    ----------
        number - Číslo pro zpracování
    Vrací:
    ------
        "+" - Pokud je číslo kladné
        "" - Pokud je číslo záporné
    """
    if (number > 0):
        return "+"
    else:
        return ""

def printPoly( array ):
    """
    Vytiskne polynom předaný jako pole
    Parametry:
    ----------
        array - Pole čísel, které se použíjí po řadě jako koeficienty polynomu
    Vrací:
    ------
        Řetězec polynomu.
    """

    length = len(array)
    output = ""

    # Projde předané pole prvek po prvku
    for i,item in enumerate(array):

        # Pokud je číslo nulové, přeskočí se
        if item == 0:
            continue
        
        # Pokud nejde o první číslo, určí se znaménko
        if i != 0:
            output += sign(item)
        
        if item != 1:
            output += str(item)
        elif item == 1 and i == 0:
            output += str(item)
        
        if i != 0:
            output += "x^" + str(i)

    return output

print( printPoly( [1, 2, 65, -2, 0, -784654, 165548 ,0 ,-5, 56 , 3, 0] ) )