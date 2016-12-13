# Zadání:
#########
#
# Newtonova (Babylónská) metoda tečen x_(i+1) = f(x_i) / f′(x_i) 
# Pro třetí odmocninu z čísla y dostáváme x_(i+1)= 1/3 (2x_i+ y/(x_i)^2)
# Řada x_i konverguje k třetí odmocnině z čísla y
# x_0 můžete nastavit na libovolnou hodnotu různou od 0, např x_0=1,
# případně na lepší odhad 
#
# Výpočet lze ukončit podle rozdílu |x_(i+1) − x_i| < presnost.
# Lze také testovat |(x_i)^3 - n| < presnost
###############################################################################

# Zadáná přesnost
prec = 1/10**8;

y = float( input("Odmocni:") );

# Výsledek
x = 1.0;
count = 0;

# Výpočet
while( abs(x**3 - count) < prec ):
    x = 1/3*(2*x + y/(x**2) );
    count += 1;

print(x);