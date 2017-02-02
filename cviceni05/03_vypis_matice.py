# Zadání:
#########
#
# Napište funkci printMatrix, která vypíše matici zadanou 2D polem.
#
# Prvky budou odděleny mezerou a každý řádek bude vypsán na nový řádek.
#
# Kromě prvků matice nebude vypsán žádný jiný znak.
###############################################################################

def printMatrix( matrix ):
    """
    Vypíše 2D pole poněkud čielnějším způsobem.
    
    Parametry:
    ----------
        matrix: list
            2D pole pro vypsání.
    """

    width = len(matrix[0])
    height = len(matrix)

    for x in range(width):
        for y in range( height ):

            # Parametr end určuje znak na konci každého volání funkce print.
            # Bez něj by se každé číslo vypsalo na nový řádek.
            print(matrix[x][y], end=" ")

        # Nový řádek.
        print()

printMatrix(
    [
        [2, 4, 7, 8],
        [8, 9, 9, 7],
        [8, 9, 9, 7],
        [8, 9, 9, 7]
    ]
)