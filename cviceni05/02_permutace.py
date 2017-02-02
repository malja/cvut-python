# Zadání:
#########
#
# Pokud pole o délce N, obsahuje všechna čísla od 0..N-1 právě jednou, pak toto
# pole kóduje permutaci tak, že první prvek se zobrazí na místo, kde se v poli 
# nachází 0, druhý prvek na místo, kde se v poli nachází 1,…
#
# Pole [0, 1, 2, 3], kóduje identickou tzv. jednotkovou permutaci o čtyřech 
# prvcích, pole [3, 2, 1, 0] kóduje otočení prvků v poli.
#
# Napište program, který načtěte z jednoho řádku standardního vstupu vektor 
# reprezentující permutaci a najde a vytiskne inverzní permutaci, tj. 
# permutaci, která převede zadanou permutaci na jednotkovou.
#
# Inverzní permutace k permutaci [2, 0, 1], je permutace [1, 2, 0], neboť první
# permutace zobrazí 0→2 a druhá permutace 2→0, obdobně 1→0, druhá permutace 
# 0→1; první 2→1 a druhá 1→2.
###############################################################################

# Pole čísel je zadáno jako uživatelský vstup. Jednotlivá čísla odděluje 
# mezera. 
array = list(map(int, input().split(" ")))

def permutate( array ):
    """
    Najde permutaci k zadanému poli. Požadavkem je, aby pole o délce N 
    obsahovalo všechny čísla od 0 do N-1. 
    
    Parametry:
    ---------
        array: list
            Pole čísel splňující požadavky popsané výše.

    Vrací:
    ------
        list
            Permutace předaného pole.
        
        False
            Pole nevyhovuje požadavkům nebo nebo má nulovou délku.
    """

    if len( array ) == 0:
        return False

    # Vytvoří pole nul o stejné délce jako má array
    temp = [0]*( len( array ) )

    # Projde všechny prvky v poli array
    for i, item in enumerate( array ):

        # V poli musí existovat prvek, jehož hodnota je stejná jako index 
        # aktuálního
        if i in array:

            # Do temp uloží aktuální prvek na místo, kde se v array nachází
            # prvek stejné hodnoty jako index aktuálního čísla. 
            temp[ array.index(i) ] = item
        else:
            return False

    return temp

print(permutate( array ) )
#print(permutate( [2, 0, 1, 4] ) ) # -> False