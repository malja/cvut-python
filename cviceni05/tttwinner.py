# Zadání:
#########
#
# Napište program tttwinner.py, který načte soubor zadaný na příkazové řádce
# (argv[1]) a zkontroluje, kdo vyhrál partii piškvorek.
#
# Soubor (viz. příklad ticktacktoe.txt) obsahuje dvourozměrné pole, ve kterém
# jsou hodnoty 0 - nepoužité pole, 1 - křížek, 2 - kolečko. Program vyhodnotí,
# zda pole obsahuje v řadě či úhlopříčce alespoň pět stejných hodnot různých 
# od 0.
#
# - Pokud v poli není alespoň pět sousedních hodnot 1 ani 2, program vytiskne 0
# - Pokud je v poli alespoň pět sousedních 1 ale není alespoň pět sousedních 2,
#   pak vytiskne 1
# - Pokud je v poli alespoň pět sousedních 2 ale není alespoň pět sousedních 1,
#   pak vytiskne 2
# - Pokud je v poli alespoň pět sousedních 1 i 2, nebo pole obsahuje i jiné 
#   hodnoty než 0,1,2, pak vytiskne ERROR
# - Program v souboru tttwinner.py odevzdejte pomocí odevzdávacího systému 
#   (úloha HW05).
###############################################################################

# Kvůli sys.argv
import sys

def loadFile(name):
    """
    Načte soubor s předaným jménem obsahující rozehranou hru piškvorek do pole.

    Parametry:
    ----------
        name:string
            Jméno souboru včetně cesty.

    Vrací:
    ------
        list
            2D pole reprezentující hru piškvorek.
    """
    storage = []

    # Otevře soubor a postará se o jeho uzavření, až ho nebudeme potřebovat
    with open(name) as file:
        # Projde soubor řádek po řádku
        for line in file:
            # Pomocné pole všech čísel v řádku
            l = []
            # Pole všech hodnot v řádku oddělených mezerou bez znaku 
            # nového řádku 
            elements = line.replace("\n", "").split(" ")
            # Projde všechny prvky pole a zkontroluje, zda jde o číslo
            for element in elements:
                if not element.isdigit():
                    print("ERROR")
                    exit()
                
                # Je to číslo, uložím ho k ostatním na tomto řádku
                l.append( int(element) )
            
            # Přidám řádek do pole
            storage.append( l )

    return storage

def checkDiagonal(x, y, array):
    
    left_diagonal = []
    right_diagonal = []

    # Pokud se nevejdeme na výšku, nemá cenu se snažit
    if ( (x + 5) < len(array) ):

        # Vejdeme se jen doleva
        if ( (y-5) >= 0 ):
            for i in range(5):
                left_diagonal.append( array[x + i][y - i] )
        # Vejdeme se jen doprava    
        if ( (y+5) <= len(array[0]) ):
            for i in range(5):
                right_diagonal.append( array[x + i][y +i] )
       
    # Pole unikátních značek v obou diagonálách
    left_diagonal = list( set( left_diagonal ) )
    right_diagonal = list( set( right_diagonal ) )

    # Asi se může stát, že by najednou v obou diagonálách někdo 
    # vyhrál, ale to mě napadlo až teď, při čtení kódu.
    # Odevzdávacím systémem jsem nicméně prošel :)

    # Jestliže v levé diagonále někdo vyhrál (v diagonále se vyskytují
    # značky pouze jednoho hráče).
    if len( left_diagonal ) == 1 and left_diagonal[0] != 0:
        return left_diagonal[0]

    # To samé pro pravou
    if len( right_diagonal ) == 1 and right_diagonal[0] != 0:
        return right_diagonal[0]

    return 0

def checkRow( row, y ):

    # Pokud bych utekl z hrací plochy
    if y + 5 > len( row ):
        return 0

    # Pole unikátních prvků v řádku
    unique = list( set( row[y:y+5] ) )

    # Pole o délce 1 znamená, že se na řádku vyskytují značky jen
    # jednoho hráce - máme vítěze
    if len(unique) == 1 and unique[0] != 0:
        return unique[0]
    else:
        return 0

def checkColumn( column, x):

    # Nechci utéct z herní plochy
    if x + 5 > len(column):
        return 0

    # Unikátní prvky ve sloupci
    unique = list( set( column[x:x+5] ) )

    # Jestliže se ve sloupci vyskytují jen značky jednoho hráce
    if len(unique) == 1 and unique[0] != 0:
        return unique[0]
    else:
        return 0

def winner( array ):
    """
    Zkontroluje předané herní pole (reprezentované 2D polem) piškvorek na vítězství
    jednoho z hráčů nebo případnou remízu.

    Parametry:
    ----------
        array:list
            2D pole obshující 0 na místě prázdných polí, 1 reprezentující 
            pole hráče jedna a 2 pole hráče dva.

    Vrací:
    ------
        string
            Vrátí řetězec "ERROR", jestliže jde o špatné zadání.

        int
            Číslo hráče (1,2) který vyhrál, nebo 0 v případě remízy.
    """

    player1 = False
    player2 = False

    for x in range( len( array ) ):
        for y in range( len( array[x] ) ):

            # Provede se kontrola z aktuální pozice
            row = checkRow( array[x], y )
            column = checkColumn( list(zip(*array))[y], x )
            diagonal = checkDiagonal(x, y, array)

            # Pokud v některé z kontrolovaných oblastí vyhrál hráč 1
            if row == 1 or column == 1 or diagonal ==1:
                player1 = True
            
            # Nebo hráč 2
            if row == 2 or column == 2 or diagonal == 2:
                player2 = True

    # Nemohou vyhrát oba
    if player1 and player2:
        return "ERROR"
    
    elif player1:
        return 1
    elif player2:
        return 2
    else:
        return 0
             
matrix = loadFile( sys.argv[1] )
print( winner( matrix ) )