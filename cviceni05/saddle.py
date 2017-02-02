# Zadání:
#########
#
# Napište program saddle.py, který načte soubor matrix.txt ve stejném adresáři
# jako je Váš skript a zjistí, zda se v této matici vyskytuje sedlový bod
# (oba typy, tj. min-max i max-min).
#
# Soubor matice.txt obsahuje matici reálných (float) hodnot m x n
#
# Sedlový bod můžete najít v podstatě dvěma způsoby: buď pro každý prvek matice
# otestujete, zda není sedlovým bodem (pomalé pro matici 1000×1000 provedete 
# 1.000.000.000 porovnání) nebo si vytvoříte pole minim pro řádky a pak pro 
# maximum ve sloupci zjistíte, zda se stejná hodnota vyskytuje jako minimum v
# nějakém řádku a pokud ano, pak průsečík tohoto sloupce a řádku je sedlový 
# bod.
#
# Program vytiskne na standardní výstup všechny sedlové body, pro každý sedlový
# bod na jeden řádek jeho pozici v matici - číslo řádku matice a číslo sloupce
# matice (počítáno od 0 - první řádek či sloupec), oddělené jednou mezerou.
#
# Program v souboru saddle.py odevzdejte pomocí odevzdávacího systému 
# (úloha HW05).
#
# Příklad
# -------
#
# Vstup:
#
"""
 1  1  2  5  6  1
 5  6  8  5  6  7
10 12 10 12 11 11
 8 10  5  6  8  9
 6  5 10 12 15 19
"""
# Výstup (pořadí řádků nerozhoduje):
#
"""
2 0
2 2
0 4
"""
###############################################################################

from re import findall

def loadFile(filename):
    """
    Načte soubor obsahující 2D pole čísel.

    Parametery:
    -----------
        filename : String
            Jméno souboru včetně přípony pro načtení

    Vrací:
    -----
        list
            2D pole obsahující všechny čísla ze souboru
    """

    storage = []

    # Otevře soubor a po ukončení práce s ním jej zavře
    with open(filename) as file:
        # Čte soubor řádek po řádku
        for line in file:
            # Do pole uloží pole čísel načtených z aktuálního řádku
            storage.append( list( map( int, findall( "[0-9.]+", line ) ) ) )

    return storage

def saddlePoints(array):
    """
    Najde všechny sedlové body v 2D poli čísel.

    Parametery:
    -----------
        array : list
            2D pole typu m x n k prohledání

    Vrací:
    ------
        list
            2D pole, jehož prvky jsou souřadnice [x, y] jednotlivých sedlových 
            bodů.
    """

    saddle = []

    # Vytvoří transponovanou matici k array
    columns = list(zip(*array))

    # Projde všechny řádky
    for x in range(len(array)):
        # Projde všechny sloupce
        for y in range( len( array[x] ) ):
            # Pokud je na souřadnici [x,y] maximum  x-tého řádku a zároveň 
            # minimum y-tého sloupce
            # Nebo je na souřadnici [x,y] minimum x-tého řádku a zároveň
            # maximum y-tého sloupce
            if ((array[x][y] == max(array[x]) and array[x][y] == min(columns[y]))
                or 
                (array[x][y] == min(array[x]) and array[x][y] == max(columns[y]))):

                # Nový sedlový bod
                saddle.append([x, y])
    
    return saddle

# Načte matici ze souboru
matrix = loadFile("matrix.txt")

# Vypíše všechny sedlové body
for i in saddlePoints(matrix):
    print("{0} {1}".format(*i))