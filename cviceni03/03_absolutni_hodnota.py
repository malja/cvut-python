# Zadani:
#########
#
# Napište funkci s jedním argumentem, která vrací absolutní hodnotu tohoto
# argumentu
#
###############################################################################

def abs( what ):
    return what if what > 0 else what * (-1)

print( abs( -27 ))