# Zadání:
#########
# Napište program, který porovná dvě funkce a(x,y,z) a b(x,y,z) se třemi 
# logickými proměnnými a zjistí, zda výrazy jsou ekvivalentní, případně
# vypíše, pro jaké kombinace vstupů se výstupy liší.
#
# Porovnejte následující dvě funkce:
###############################################################################

def f(x,y,z):
    return (x and y) or (not y and z)
 
def g(x,y,z):
    return x or z

###############################################################################

for a in (True, False):
    for b in (True, False):
        for c in (True, False):
            if f( a, b, c) != g(a, b, c):
                print("Lisi se pro: x: ", a, ", y:", b, ", z: ", c)
