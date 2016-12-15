# Zadání:
#########
#
# Napište funkce gcd1 a gcd2, které vrátí největšího společného dělitele a 
# počet kroků, které k výpočtu potřebovaly.
#
# Funkce gcd1 bude počítat největšího společného dělitele čísel a a b takto:
# - Dokud a není rovno b
#   - Je-li a větší než b
#     - a = a-b
#   - jinak
#     - b = b-a
# a i b jsou největší společný dělitel původních čísel
#
# Funkce gcd2 bude počítat největšího společného dělitele čísel a a b takto:
# - Dokud b není rovno nule
#    - t = b
#    - b = a mod b
#    - a = t
# a je největší společný dělitel původních čísel
#
# Zjistěte kolik kroků potřebuje gcd1 a gcd2 pro spočtení největšího společného
# dělitele 6997193, 18992381 a dvojice 361, 18992381
###############################################################################

# První verze
def gcd1( a, b ):

    # Počítadlo kroků
    counter = 0

    while ( a != b ):

        counter += 1

        if ( a > b ):
            a = a-b
        else:
            b = b - a
    
    # Vrací největšího společného dělitele a počet kroků k jeho nalezení
    return a, counter

# Druhá verze
def gcd2( a,b ):

    # Počítadlo kroků
    counter = 0

    while( b != 0 ):
        counter += 1

        a, b = b, a % b

    # Vrací největšího společného dělitele a počet kroků k jeho nalezení
    return a, counter

print( gcd1(6997193, 18992381), "a", gcd2(6997193, 18992381) )
print( gcd1(361, 18992381), "a", gcd2(361, 18992381) )
