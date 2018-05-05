# Zadání: 
#########
#
# Pravidla hry jsou jednoduchá:
# - Pokud jsou v okolí jedné buňky živé právě 3 buňky, 
#   pak v této buňce život vznikne (nebo zůstane)
# - Pokud je buňka živá a v jejím okolí jsou právě 2 živé buňky,
#   pak tato buňka bude žít i nadále
# - V ostatních případech buňka zahyne buď na osamění, nebo přemnoženost
#
# Budeme uvažovat uzavřený svět, tedy sousední políčko pro první pole řádku
# je poslední pole řádku, sousední pole pro první řádek je poslední řádek.
#
# Napište program, který bude simulovat 40 kroků hry life pro toto počáteční 
# pole:
"""
a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   ]
"""

############################################################################################ NEFUNGUJE!!!! ######################################################################################################

import time

# Výchozí stav
a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   ]

def neighbours( x, y, world ):
    """
    Získá počet sousedů dané buňky.

    Parametry:
        x (int)         X-ová souřadnice
        y (int)         Y-ová souřadnice
        world (list)    2D pole s aktuálním stavem.

    Vrací:
        int Počet sousedů buňky na souřadnicích [x;y]
    """

    # Počet sousedů
    count = 0

    # maximální souřadnice na x-ové ose
    x_max = len(world[0])-1
    # maximální souřadnice na y-ové ose
    y_max = len(world)-1

    # Poznámka: Hodí se říct, že souřadnice mají počátek v levém horním rohu.
    # Směrem doprava postupuje souřadnice x a směrem dolů se zvětšuje
    # souřadnice y.
    # Pro získání y-tého řádku: world[y]
    # Pro získání x-tého prvku y-tého řádku: world[y][x]

    # Souřadnice J reprezentuje x-ovou souřadnici a K tu y-ovou.
    for j in range(x-1, x+2):
        for k in range(y-1, y+2):

            # Buňka si nemůže být sama sousedem
            if j == x and k == y:
                continue

            # Snažím se zasahovat do x-ové souřadnice mimo hrací pole
            if j < 0: 
                # len(world[0]) vrátí počet prvků. Protože ale j bude
                # rovno -1 nebo méně (-2), dostanu se tímto vždy na
                # poslední (předposlední) index v rámci řádku
                j = len(world[0])+j

            # Snažím se na x-ové ose zasahovat mimo hrací pole
            if j > x_max:
                # Přetečení zpět na začátek
                j = 0

            if k < 0:
                k = len(world)+k

            if k > y_max:
                k = 0

            # Pokud je na k,l souřadnicích v předchozím kroku 1, přičte se,
            # v opačném případě se nic neděje :)
            count += world[k][j]
    
    return count

def life_step( world ):
    """
    Vygeneruje jeden krok hry Life.

    Parametry:
        world (list)    2D pole obsahující předchozí krok hry.

    Vrací:
        list    Aktuální krok
    """

    # Vytvoření prázdného kroku
    # Jde o in-line for cyklus. Pro každý řádek z proměnné world se vytvoří
    # pole nul o délce originálního řádku.
    state = [[0]*len(i) for i in world]

    # Projde se celý předchozí krok
    for y in range( len(world) ):
        for x in range( len(world[0]) ):

            # Zjistí se počet sousedů daného políčka
            n = neighbours( x, y, world )
            
            # Pokud jsou v okolí políčka tři živé buňky, vznikne život
            if n == 3:
                state[y][x] = 1
            # Pokud je buňka živá a má právě dvě sousední živé buňky, přežije
            elif n == 2 and world[y][x] == 1:
                state[y][x] = 1
            # Buňka zahynula na přemnožení nebo osamocení
            else:
                state[y][x] = 0

    return state

def life( world, max_steps = 1 ):
    """
    Vygeneruje zadaný počet kroků hry život.

    Argumenty:
        world (list)        Výchozí stav pro hru Life. Jde o 2D pole, kde hodnota 1 znamená
                            přítomnost buňky a hodnota 0 prázdné políčko.

        max_steps (int)     Maximální počet kroků, které se mají vygenerovat.

    Vrací:
        list    Pole obsahující 2D pole s jednotlivými kroky hry Life. Index je číslo dané
                generace.
    """

    # Seznam se všemi kroky hry
    steps = []
    
    # Jako první krok se přidá výchozí stav
    steps.append( world )

    # Projde všechna čísla od 0 do max_steps (bez)
    for i in range(max_steps):
        # Do seznamu všech kroků přidá jeden nový. Parametr steps[i] vždy předá funkci
        # life_step obsah předchozíko kroku. (i se počítá od 0, ale na ní je výchozí stav).
        steps.append( life_step( steps[i] ) )

    return steps

if __name__ == "__main__":

    # Vygenerování 50 iterací hry Live.
    generations = life(a, 50)

    # Výpis všech generací s rozestupem 0.5s.
    # i             Číslo generace
    # generation    Pole s jednou generací
    for i, generation in enumerate(generations):

        print("Generace", i)

        # Výpis aktuální generace
        for y in range(len(generation)):
            for x in range(len(generation[0])):
                if generation[y][x] == 1:
                    print("X", end="")
                else:
                    print("_", end="")
            print()

        print("\n\n")
        time.sleep(0.5)



