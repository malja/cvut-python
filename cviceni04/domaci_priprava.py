# Zadání:
#########
# 
# Implementujte následující úlohy:
#
# - swap(a,b), která navzájem vymění tyto dva prvky
# - Napište funkci, která vypisuje 1,-1,1,-1 …
# - Napište funkci, která vypisuje výsledek operace (−1)^k pro k=0,…,100.
#   Zamyslete se nad rychlostem výpočtu, navrhněte alternativní postupy
# - Napište funkci min(a,b), která vrací minimum ze těchto dvou prvků
# - Napište funkci max(a,b)
# - Napište funkci area(radius), která vypočítá obsah kruhu o zadaném poloměru
# - Napište funkci d2r(angle), která převede stupně na radiány 
# - Napište funkci r2d(angle), která převede radiány na stupně
# - Napište funkci normalize(angle), která převede zadaný úhel (v radiánech) 
#   do intervalu <0,2π).
# - Napište funkci pro výpis pole:
#   - s využitím cyklu for
#   - s využitím cyklu while
###############################################################################

import math

def swap( a, b ):
    """
    Prohodí prvky a, b.
    """
    a,b = b,a

def plusminus():
    """
    Do nekonečna a ještě dál vypisuje 1, -1, 1, ...
    """
    i = 1
    while True:
        print(i)
        i = -i


def weirdo( iterations = 100 ):
    """
    Vypisuje výsledek (-1)^k. Teoreticky pomalejší verze.
    """
    for i in range( iterations+1 ):
        print( (-1)^i )

def weirdo2( iterations = 100):
    """
    Vypisuje výsledek (-1)^k. Teoreticky rychlejší verze.
    """
    for i in range( iterations+1 ):
        if i%2 == 0:
            print( 1 )
        else:
            print( -1 )

def min( a, b ):
    """
    Vrátí menší ze dvou hodnot.
    """
    return a if a < b else b

def max( a, b ):
    """
    Vrátí větší ze dvou hodnot
    """
    return a if a > b else b

def area( radius ):
    """
    Vypočítá obsah kruhu.
    """
    return math.pi * radius ** 2

def d2r( angle ): 
    """
    Převede stupně na radiány
    """
    return angle * ( math.pi/180 )

def r2d( angle ):
    """
    Převede radiány na stupně
    """
    return angle * (180/math.pi)

def normalize( angle ):
    """
    Převede zadané radiany na interval <0, 2pi)
    """
    return angle%(2**math.pi)

def printArray( array ):
    """
    Vypíše prvky pole pomocí for
    """
    for element in array:
        print( element )

def printArray2( array ):
    """
    Vypíše prvky pole pomocí while
    """
    i = 0
    while i < len(array):
        print( i )
        i += 1




