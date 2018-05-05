import copy

# Rozdělí řádek na inputu na jednotlivé části oddělené mezerou.
# Každá část je zatím jako řetězec
array = input().split(" ")

# Přichystáme si potřebné proměnné
minimum = int( array[0] )   # Minimum
maximum = int( array[0] )   # Největší číslo
maximum2 = 0                # Druhé největší číslo != maximum
sum = 0                     # Suma všech čísel
count = 0                   # Počet čísel majících na pozici desítek 3,4,5

# Projde všechny prvky
for i in array:

    # Přetypuje na int
    element = int( i )

    # Zvýši sumu
    sum += element

    # element je menší než minimum
    if minimum > element:
        minimum = element

    # element je větší než max
    if maximum < element:
        
        # Uložíme si staré maximum pro kontrolu
        alternative_max = copy.deepcopy( maximum )
        maximum = element

        # Pokud je druhé maximum menší než to, které jsme právě odstranili
        # Asi netřeba testovat, mělo by to tak být vždy
        if alternative_max > maximum2:
            maximum2 = alternative_max

    # element je Větší než alternativní max
    elif maximum2 < element and element != maximum:
        maximum2 = element

    # Pokud má řetězec s číslem délku větší než 2 (tzn. mohl by mít desítky)
    if len( i ) >= 2:

        # Znak na pozici desítek. Asi by šlo přetypovat na int, ale muselo by
        # se ošetřit případ, kdy na této pozici bude mínus.
        x = i[-2]
        
        # Na pozici desitek je 3, 4 nebo 5
        if x == "3" or x == "4" or x == "4":
            count += 1 

# Zadání:
# Na standardní vstup bude vložen řádek s čísly oddělenými mezerou.
#    
# Výpis ve formátu:
# - Nejmenší číslo
# - Průměrná hodnota všech čísel
# - Rozdíl mezi maximem a druhým největším číslem. Pokud se vyskytuje vícekrát číslo obsažené v maximum,
#   musí být číslo v maximum2 od něj rozdílné. Tzn. nejde, aby maximum == maximum2.
# - Počet čísel, které mají na pozici desítek 3,4,5.

# Testovací vstup:
# 341 71 -400 -53 116 -302 536 -375 -301 295 229 -264 516 438 183 536
#
# Výstup:
# -400
# 97.875
# 20
# 5

print( minimum )
print( sum / len(array) )
print( maximum - maximum2 )
print( count )
