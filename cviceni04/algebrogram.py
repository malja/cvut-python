# Zadání:
#########
#
# Napište program algebrogram.py, který řeší jednořádkový algebrogram.
#
# Algebrogram používá pouze sčítání a pouze na levé straně rovnice.
# Úkolem je najít takovou záměnu písmen za cifry tak, aby žádná dvě písmena
# neměla stejnou hodnotu a žádné číslo nezačínalo 0.
#
# Algebrogram bude zadán na jednom řádku standardního vstupu, 
# např: send+more=money a výstupem Vašeho programu bude řešení tohoto 
# algebrogramu ve formátu dosazených cifer: 9567+1085=10652
#
# Algebrogram bude zadan bez mezer (tedy 'a+b=c', nikoliv 'a + b = c').
#
# Sčítance se vyskytují pouze na levé straně rovnice a jejich počet není 
# omezen.
#
# Pokud má algebrogram více řešení, vytiskněte všechny (netiskněte ale 
# vícekrát stejné řešení)
#
# POZOR: Program je výpočetně náročnější, otestujte si nejdříve Váš program
# na počítači a pouze důkladně otestovaný program nahrávejte do odevzdávacího
# systému
###############################################################################

from re import findall
from itertools import permutations

algebrogram = input()

def solveAlgebrogram( algebro ):
    """
    Vyřesí algebrogram předaný v řetězci
    Parametry:
    ----------
        algebro - Řetězec se zadáním.
    Vrací:
    ------
        Pole s řešeními
    """

    solutions = []

    # Pouze kvůli evalu
    algebro = algebro.replace("=", "==")

    # Získá všechna slova
    words = findall("[A-Za-z]+", algebro)
    
    # Z nich udělá pole všech neopakujících se písmen
    chars = set("".join(words) )
    
    # První písmena, nesmí být rovna nule
    firstChars = set(w[0] for w in words) 
    
    
    chars = "".join(firstChars) + "".join(chars - firstChars)
    
    # Počet prvních znaků
    firstCharsNum = len(firstChars)

    # Projde všechny permutace čísel 0 až 9 o celkové délce len(chars)
    for perm in permutations('0123456789', len(chars)):

        # Pokračujeme jen pokud není na prvních firstCharsNum pozicích nuly
        if '0' not in perm[:firstCharsNum]:

            # Velké černé zlé woodoooooooooooo
            transmutation = str.maketrans(chars, ''.join(perm))

            # Dosadíme do původní hádanky naše čísla místo písmen
            equation = algebro.translate(transmutation)
            
            # Zkusíme, jestli rovnice platí
            try:
                if eval(equation):
                    
                    # Už nebudeme porovnávat, tak můžeme vrátit rovná se
                    solutions.append( equation.replace("==", "=") )
            
            except ArithmeticError:
                pass

    return solutions

solutions = solveAlgebrogram(algebrogram)
for solution in solutions:
    print(solution)