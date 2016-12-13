# Zadání:
#########
#
# Program načte kladné reálné číslo (označme ho x) a poté načte další kladné
# reálné číslo (označme ho y).
# Program vypočte logaritmus čísla x o základu y metodou půlení intervalu.
# Výsledek nalezněte s přesností na 8 desetinných míst (výpočet ukončíte
# pokud |x1−x2|<0.000000001.
# Použití nějaké knihovní funkce (např. math.log) není dovoleno. Program 
# volající cizí funkce nebude hodnocen.
#
# Pro nastavení krajních mezí platí následující pomůcky:
# - pokud je y>1 a x>1, pak levá mez může být 0
# - pokud je y>e a x>1, pak víme, že y^k>k+1, tedy pravá mez může být x
# - pokud je e>y>1 a x>1, pak víme, že y^k > k*ln(y)+1 (derivace v bodě 0 je 
#   ln(y)), tedy pravá mez může být x/ln(y) a pro e>y>1 můžeme použít
#   ln(y) > (y−1)/(e−1)
# - pokud je x<1 pak víme, že 1/x > 1 a 1/(y^k) = y^(−k), tím pádem můžeme 
#   použít záporné hodnoty mezí zjištěné pro hodnotu 1/x, tedy pro výše 
#   uvedené případy pravá mez rovna 0 a levá mez rovna −1/x, resp. 
#   (−1/x) * ( (e−1)/(y−1) )
# - pokud je y<1, pak (1/y)^k = y^(−k). Tedy zjistíme meze pro základ 1/y
#   (což jsme uvedli výše) a tyto meze vynásobíme −1.
###############################################################################

x = float(input())  # log
y = float(input())  # zaklad

# Funkce pro výpočet logaritmu
def log(z, base, precision = 10 ** -9):

    lower_limit = 0.0
    upper_limit = z

    e = 2.7182818284

    # Kontrola mezí.
    # Hodnoty jsou výsledkem několika hodin metody pokus-omyl.
    if base < 0 or base == 1:
        raise ValueError('Logaritmus není pro záporný základ, nebo základ roven 1 definován')

    if (base < e) and (base > 1.0) and (z > 1.0):
        upper_limit = (z - 1) / ((base -1)/ e )
    elif z < 1.0:
        upper_limit = 0.0
        lower_limit = (-1/z) * ((e-1)/(base-1))

    if base < 1.0:
        upper_limit = 0
        lower_limit = (1/z)

    if z > 1.0 and (base < 1.0):
        upper_limit = -(1/base) * z

    if (base < 1.0) and (z < 1.0):
        upper_limit = 150
        lower_limit = -150

    logarithm = 0.0

    # Výpočet samotného logaritmu
    while abs(lower_limit - upper_limit) > precision:

        if (base < 1.0) and (z < 1.0):
            logarithm = abs( (lower_limit + upper_limit)/2 )
        else:
            logarithm = (lower_limit + upper_limit) / 2

        if base ** logarithm < z:
            lower_limit = logarithm
        else:
            upper_limit = logarithm

    return logarithm

# Výpis logaritmu v požadovaném formátu
print("{0:.9f}".format(round( log(x,y), 9)))
