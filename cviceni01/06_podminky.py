# Zadání:
#########
#
# Upravte program z úlohy 5 tak, aby:
# - načetl vstupní číslo z příkazové řádky
# - vytiskl ANO, pokud je hodnota vzorce stejná jako součet nebo
#   vytiskne NE

# Načtení čísla pro výpočet třetí mocniny
x=int(input())

# Výpočet pomocí sumy
sum=0
for k in range( x+1 ):
    sum+=k**3

# Výpočet vzorcem
sum1= ((x*(x+1))/2)**2

if sum == sum1:
    print("ANO")
else:
    print("NE")
