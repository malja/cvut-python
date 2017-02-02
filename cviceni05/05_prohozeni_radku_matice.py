# Zadání:
#########
#
# Napište program, který načte matici a následně permutaci, která definuje 
# prohození řádků zadané matice. Na výstup program vytiskne matici s řádky 
# prohozenými podle zadané permutace.
###############################################################################

matrix_input = input("Matice (čísla odděluj mezerou, řádky čárkou):").split(",")
permutation = list( map( int, input("Permutace (čísla odděluj mezerou):").split(" ") ) )

# Pouze zpracuje zadanou matici tak, aby s ní mohl python pracovat
matrix = []
for m in matrix_input:
    matrix.append( list(map(int, m.split(" ") ) ) )

def swap( perm, matrix ):
    """
    Prohodí řádky matice podle zadané permutace.

    Parametry:
    ----------
        perm: list
            Pole délky N obsahující čísla od 0 do N. Určuje permutaci,
            se kterou se prohodí řádky matice.

        matrix: list
            Pole, ve kterém se prohodí řádky.
    """
 
    if len(perm) != len(matrix):
        return None

    # Vytvoří pole stejné velikosti jako předaná matice
    result = [0] * len(matrix)

    # Projde matici
    for i in range( len( matrix ) ):
        
        # Pokud v poli permutací není aktuální index,
        # nevíme kam řádek umístit
        if not i in perm:
            return None

        # Prohodí řádek na správné místo
        result[ perm.index(i) ] = matrix[i]

    return result

print( swap( permutation, matrix ) )

        


        