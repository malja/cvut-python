# Zadání:
#########
# Napište funkci, která vrací největší hodnotu v poli a zároveň vrací index
# tohoto prvku.
#
# Pro pole nulové délky vrací index -1.
#
# Pozor: je třeba předpokládat, že v poli mohou být jakékoliv hodnoty 
# (kladné, nuly, záporné)!
###############################################################################

array = input("Čísla (odděluj mezerou): ").split(" ")

def max_in_array(arr):
    """
    Funkce nalezne největší hodnotu v poli předaném jako parametr.
    Parametry:
    ----------
        arr - Pole čísel k prohledání
    Vrací:
    ------
        maximální hodnotu
    """
    maxNum = 0

    for i in array:
        if maxNum < int(i):
            maxNum = int(i)

    return maxNum

print(max_in_array(array))