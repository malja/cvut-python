# Zadání:
#########
# 
# Napište program, který načte číslo n a vypíše jeho nejmenšího dělitele
# různého od 1.
# Je vhodné použít konstrukci break, cyklus můžeze použít while i for.
#
# Otestujte svůj program na čísle 999962000357
###############################################################################

number = 999962000357;
divisor = 2;

# (number%divisor) - pro sudé číslo vrací 0, pro liché 1
# (divisor<number/divisor) - dělitel musí být menší
while ((number%divisor) and (divisor<number/divisor)):
    divisor+=2;

print( divisor );