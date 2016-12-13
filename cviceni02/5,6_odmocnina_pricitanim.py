# Zadání:
#########
# 
# Vypočtěte třetí odmocninu kladného čísla y, zadaného jako vstup Vašeho
# programu následujícím postupem:
# - Přičítejte k proměnné value číslo 1 dokud je třetí mocnina této proměnné
#   menší než y
# - Přičítejte k proměnné value číslo 0.1 dokud je třetí mocnina této 
#   proměnné menší než y
# - Přičítejte k proměnné value číslo 0.01 dokud je třetí mocnina této
#   proměnné menší než y
# Proměnná value obsahuje odmocninu čísla y s přesností na dvě desetinná čísla
###############################################################################

# Zadání 2:
###########
#
# Upravte program tak, aby pracoval se zadanou přesností.
# - Program načte číslo y a n a nalezne třetí odmocninu z čísla y na n desetinných míst
# - Upravte algoritmus, aby uměl spočítat i třetí odmocniny ze záporných čísel

print("Script na výpočet třetí odmocniny Vámi zadaného čísla pomocí přičítání.")
y = int( input("Zadejte kladné číslo, jehož třetí odmocnina Vás zajímá:"))
prec = int( input("Zadejte počet desetinných míst, na který se má odmocnina vypočítat:"))
k = 0
step = 1

if y < 0:
    print("Odmocnina ze záporného čísla není pro reálná čísla definována.")
    exit()

for p in range( prec ):
    while (k+step)**3 <= y:
        k += step
    
    step /= 10

print( "Odmocnina Vámi zadaného čisla", y, "je", k, "s přesností na", prec, "desetinných míst." )