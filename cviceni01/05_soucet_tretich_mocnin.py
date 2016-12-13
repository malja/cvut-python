# Zadání:
# Napište program, který spočítá sumu třetích mocnin:
# 
#     n
#     __
#     \_  k^3
#     /_ 
#     k = 0
#
# Poté program upravte tak, aby zkontroloval, zda se součet třetích 
# mocnin rovná vzorci:
#
#   n(n+1)
# ( ------ ) ^ 2
#     2
#
# Program vytiskne na jednu řádku součet třetích mocnin a na další
# výsledek podle vzorečku.
#
# Vytištené výsledky musí být celá čísla!

# Načtení čísla pro výpočet třetí mocniny
x=int(input())

# Výpočet pomocí sumy
sum=0
for k in range( x+1 ):
    sum+=k**3

# Výpočet vzorcem
sum1= ((x*(x+1))/2)**2

print( int( sum ) )
print( int( sum1 ) )

