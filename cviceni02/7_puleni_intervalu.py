# Zadání:
#########
# 
# Metoda půlení intervalu hledá řešení obecné rovnice f(x)=0, kdy známe
# dva body x1 a x2 takové, že f(x1)<0 a f(x2)>0.
#
# - Algoritmus rozpůlí interval mezi body x1x1 a x2x2, tedy nalezne bod 
#   x′=(x1+x2)/2 a pokud je f(x′)<0 pak nahradí bod x1 bodem x′, jinak 
#   nahradí bod x2 bodem x′.
# - Výše uvedený krok se opakuje dokud není |x1−x2| < presnost
#
# V případě hledání třetí odmocniny z čísla y je f(x)=x3−y, pokud f(x)=0,
# tak to znamená, že x3−y=0, což lze zapsat jako x^3=y tedy 
# x = sqrt(y, 3)
#
# Napište program, který nalezne třetí odmocninu zadaného čísla y na 8
# desetinných míst (výpočet ukončíte pokud |x1−x2|<0.000000001). 
# Na počátku zvolte x1=0 a x2=y pro kladná y>1 a x1=y a x2=0x2=0 pro záporná
# y←1 a x1=−1 a x2=1 v ostatních případech.
###############################################################################

# Pevně daná přesnost
prec = 10 ** -8

y = float(input("Zadejte hodnotu čísla y:"))

# Odmocnina z nuly je nula
if y == 0:
    print("0")

# Nastavení podmínek dle zadání
if y > 0:
    x1 = 0.0
    x2 = 1.0

    if y >= 1.0:
        x1 = 1.0
        x2 = y

elif y >= -1.0:
    x1 = -1.0
    x2 = 0.00
else:
    x1 = y
    x2 = -1.0

x = 0

# Samotný výpočet
while abs(x1 - x2) > prec:

    # Střed
    x = (x1 + x2) / 2

    # Pokud je střed menší než hledané číslo
    if x ** 3 < y:
        # Dolní mez nastaví na střed
        x1 = x
    else:
        # Horní mez nastaví na střed
        x2 = x

print(x)
