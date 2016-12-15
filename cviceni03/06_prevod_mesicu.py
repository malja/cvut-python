# Zadání:
#########
#
# Napište funkci convert_num_to_month, která dostane jako parametr pořadové
# číslo měsíce v roku a vrátí jeho jméno.
#
# Napište funkci convert_month_to_num, která dostane jako parametr jméno měsíce
# v roku a vrátí jeho pořadové číslo v roce.
# POZOR: leden má číslo 1, prosinec 12
#
# Tuto funkci použijte v programu, který načte řetězec a pokud je první znak 
# písmeno a vytiskne na obrazovku číslo měsíce, pokud je první znak číslo 
# vytiskne název měsíce
#
# Pomůcka: V programu můžete využít následující proměnnou:
# month=['leden','unor','brezen','duben','kveten','cerven','cervenec','srpen','zari','rijen','listopad','prosinec']
###############################################################################

month=['leden','unor','brezen','duben','kveten','cerven','cervenec','srpen','zari','rijen','listopad','prosinec']

def convert_num_to_month( number ):
    if number < 1 or number > 12:
        return None

    return month[number - 1]

def convert_month_to_num( name ):
    if not name in month:
        return None

    return month.index(name)+1

# Příklad špatného vstupu
print( convert_month_to_num("bramborník"), convert_num_to_month(14) )

# Příklad dobrého vstupu:
print( convert_month_to_num("duben"), convert_num_to_month(10) )
