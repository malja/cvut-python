# Zadání:
#########
#
# Napište program, který načte celé číslo udávající časový interval ve¨
# vteřinách a vypíše kolik je to dní, hodin, minut a vteřin.
#
# Pro vstup:
# 100000
# bude výstup:
# den 1 hodin 3 minut 46 vterin 40
###############################################################################

# Počet vteřin
seconds = int(input("Zadej počet vteřin:"))

# Přepočet
mins = seconds // 60
hours = mins // 60
days = hours // 24

# Výpis. 
# Funkce format nahradí {x} za odpovídající hodnotu parametru s indexem X
print("den {0} hodin {1} minut {2} vterin {3}".format(days, hours%24, mins%60, seconds%60))