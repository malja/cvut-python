# Zadání:
#########
#
# Napište funkci polyValue , která pro zadaný polynom a hodnotu x vypočte jeho
# hodnotu v zadaném bodě x.
# 
# Tedy polyValue([1,0,2], 4) má hodnotu 33, protože 1+2*x^2=1+2*16=33
#
###############################################################################


def polyValue( array, x_value ):
    """
    Výpočet hodnoty polynomu. Za neznámou dosazuje x_value
    Parametry:
    ----------
        array - Pole čísel použité jako koeficienty polynomu
        x_value - Hodnota pro dosazení za neznámou
    Vrací:
    ------
        Hodnota zadaného polynomu.
    """
    value = 0

    for i, element in enumerate( array ):
        value += element * x_value ** i

    return value

print( polyValue([1,0,2], 4) )
        