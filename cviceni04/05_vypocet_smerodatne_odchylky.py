# Zadání:
#########
#
# Pro výpočet směrodatné odchylky, potřebujete znát střední hodnotu, kterou
# spočtete jako aritmetický průměr hodnot v poli. Napište funkci getMean, 
# která vypočte střední hodnotu zadaného pole.
#
# Napište funkci getDeviation, která vypočte směrodatnou odchylku, ve funkci
# použijte volání funkce getMean
#
# Směrodatná odchylka je: σ^2 = 1/n * sum_(i=i)^n (x_i − E(x) ) kde E(x) je 
# střední hodnota vypočtená funkcí getMean.
###############################################################################

import math

# Rozdělí vstup na pole čísel
numbers = list( map( int, input("Hodnoty:").split(" ") ) )

def getMean( array ):
    """
    Funkce vrátí aritmetický průměr čísel v předaném poli.
    Parametry:
    ----------
        array - Pole čísel pro zpracování
    Vrací:
    ------
        Aritmetický průměr čísel v poli
    """

    # Ochrana před dělením nulou
    if len(array) == 0:
        return 0

    sum = 0
    
    # Sečte všechny hodnoty v poli
    for element in array:
        sum += element

    # Vrátí aritmetický průměr čísel
    return sum/len(array)

def getDeviation( numbers ):
    """
    Vypočte směrodatnou odchylku předaných čísel.
    Parametry:
    ----------
        numbers - Pole čísel pro zpracování
    Vrací:
    ------
        Směrodatná odchylka
    """

    # Suma
    deviation = 0

    # Počet prvků
    n = len(numbers)

    # Střední hodnota
    mean = getMean( numbers )

    for x in numbers:
        deviation += ( ( x - mean) ** 2)

    # Vrací se odmocnina z jedné n-tiny sumy
    return math.sqrt( (1/n) * deviation )

print( getDeviation(numbers) )