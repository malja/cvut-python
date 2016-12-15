# Zadání:
#########
#
# Program přečte ze standardního vstupu celé kladné číslo v rozsahu 0 až 99
# (označme ho k).
#
# Program vytiskne tabulku udávající soudělnost čísel m,n=1,…,k
# Pokud jsou číslat m,n soudělná, vypíše se na n-tém řádku a m-tém sloupci
# 'x', jinak vytiskne '.'
# 
# Program pro úlohu HW03 pojmenujte commensurable.py
#
# Pokud není na vstup zadáno celé kladné číslo v rozsahu 0 až 99, vypíše 
# program ERROR a skončí
#
# Pozn. Čísla jsou soudělná, jestliže jejich největší společný dělitel je větší
# než 1. Např. pro vstup 10 program vytiskne:
#
# ..........
# .x.x.x.x.x
# ..x..x..x.
# .x.x.x.x.x
# ....x....x
# .xxx.x.xxx
# ......x...
# .x.x.x.x.x
# ..x..x..x.
# .x.xxx.x.x
###############################################################################

#Vstup má být číslo od 0 do 99
k = input()

# Je třeba otestovat, zda je opravdu o číslo
try:
    k = int(k)
except ValueError:
    print("ERROR")
    exit()

# a zda je v zadaném rozsahu
if k < 0 or k > 99:
    print("ERROR")
    exit()


#Funkce pro nalezení největšího společného dělitele
def gcd( a,b ):

    while( b != 0 ):
        a, b = b, a % b

    return a

# Pokud je číslo n a m soudělné, vypíše x, jinak .
for n in range(1, k+1):
    for m in range(1, k+1):
        if gcd(n, m) > 1:
            print("x", end="")
        else:
            print(".", end="")
    print()