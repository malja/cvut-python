# Zadání:
#########
#
# Napište program, který načte soubor předaný jako první parametr příkazové 
# řádky. Ten bude obsahovat dvojice desetinných čísel, vždy jednu na 
# řádku. Hodnoty reprezentují body ve 2D.
#
# Vaším úkolem je:
#
# 1) Vypsat na standardní výstup X a Y souřadnice bodu, který je nejdále
#    od nuly.
# 2) Vypsat indexy (odpovídají číslům řádků v souboru, počítáno od 0)
#    dvou nejbližších bodů.
# 3) Vypsat souřadnice těžiště. 
#
###############################################################################

import sys # Kvůli sys.argv
import math # Kvůli math.sqrt


def loadFile( filename ):
    """
    Načte soubor se zadaným jménem do 2D pole.
    Každý prvek pole obsahuje popořadě: X-ovou souřadnici, Y-ovou souřadnici
    a vzdálenost od bodu [O, O].

    Parametry:
    ----------
        filename: string
            Řetězec se jménem souboru.

    Vrací:
    ------
        list
            2D pole se načtenými body.
    """
    coords = []

    # Konstrukce with se postará o zavření souboru po ukončení načítání
    with open( filename ) as file:

        # Projde soubor řádek po řádku
        for line in file:

            # Rozdělí řádek podle mezery na pole o dvou prvcích. Ty
            # pak přetypuje na float.
            line = list( map(float, line.split(" ") ) )

            # Vypočítá vzdálenost od bodu [0, 0] a uloží jí jako třetí
            # hodnotu k souřadnicím
            line.append( math.sqrt( line[0]**2 + line[1]**2 ) )

            # Uloží aktuální bod
            coords.append( line )

    return coords

def getFurtherFromZero( array ):
    """
    Vyhledá v poli bod s nejvyšší vzdáleností od bodu [0, 0].

    Parametry:
    ----------
        array: list
            Pole s hodnotami.

    Vrací:
    ------
        list
            Pole obsahující bod, jenž je od [0, 0] nejdál.
    """

    # Sorted seřadí pole dle zadaného kritéria.
    # reverse=True - Řadí od největšího po nejmenší
    # key= ... - Řadí podle třetího prvku pole
    return sorted( array, key=lambda a: a[2], reverse=True)[0]    

def centerOfGravity( array ):
    """
    Vypočítá ze zadaých bodů jejich těžiště.

    Parametry:
    ----------
        array: list
            Pole s body.

    Vrací:
    -----
        list
            Pole s X- a Y-ovou souřadnicí těžiště.
    """

    sum_X = 0
    sum_Y = 0

    # Sečte X-ové a Y-ové souřadnice všech bodů
    for element in array:
        sum_X += element[0]
        sum_Y += element[1]

    # Vratí průměr.
    return sum_X/len(array), sum_Y/len(array)


def closestPoints( array ):
    """
    V poli najde dva vzájemně nejbližší body a vrátí jejich indexy.

    Parametry:
    ----------
        array: list
            Pole s body.

    Vrací:
    ------
        list
            Pole se indexy dvou vzájemně nejbližších bodů.

    """

    a_index = 0
    b_index = 0
    min_dist = -1

    # Pro každý prvek pole
    for x in range( len(array) ):
        # Projde všechny prvky pole ještě jednou
        for y in range( len(array) ):
            
            # Nebudeme porovnávat vzdálenost prvku se sebou samým
            if x == y:
                continue

            # Vzdálenost dvou bodů
            d  = math.sqrt( (array[x][0] - array[y][0])**2 + (array[x][1] - array[y][1])**2 )
            
            # Pokud jde o první vzdálenost
            if min_dist == -1:

                # Rovnou se použije
                min_dist = d
                a_index = x
                b_index = y

                continue

            # ... jinak
            else:

                # Porovnáme s posledně uloženou vzdálenosti
                if min_dist > d:
                    
                    # ... a data uložíme jen pokud jsme našli lepší shodu. 
                    min_dist = d
                    a_index = x
                    b_index = y

    return a_index, b_index
            

# Načte soubor
data = loadFile( sys.argv[1] )

# Najde nejvzdálenější bod od [0,0]
further = getFurtherFromZero(data)
print( further[0], further[1])

# Najde indexy dvou vzájemně nejbližších bodů
closest = closestPoints( data )
print( closest[0], closest[1] )

# Najde těžiště
center = centerOfGravity( data )
print( center[0], center[1] )