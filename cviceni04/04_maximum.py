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

array = list( map(int, input("Čísla (odděluj mezerou): ").split(" ") ) )

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

    if len(arr) == 0:
        return -1

    maxNum = arr[0]
    index = 0

    for i, element in enumerate(arr):

        if maxNum < int(element):
            maxNum = int(element)
            index = i

    return maxNum, index

print(max_in_array(array))