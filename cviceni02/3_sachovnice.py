# Zadání:
#########
#
# Napište program, který vytiskne čtvercovou šachovnici ze znaků 'O' a '*'
# o velikosti zadané uživatelem, jako vstup Vašeho programu.
# Pro tisk znaku bez konce řádky použijte následující konstrukci. 
# end definuje zakončení řetězce a je standardně nastaven na \n
#
# print(".", end="")
###############################################################################

# Velikost šachovnice
size = int( input("Velikost sachovnice:") );

# Pro všechny řádky
for x in range( size ):
    # Pro všechny sloupce
    for y in range( size ):
        # Pokud je číslo sudé
        if ( (x+y)%2 == 0 ):
            print( "#", end="");
        # ... nebo liché
        else:
            print( "O", end="");
            
    # Na konci řádku vytiskne nový řádek
    print();
        